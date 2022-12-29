"""
IndexError: list index out of range: I have used Pixabay for images. For some keywords, there is no images on pixabay. Please change the keywords at this situation. Try to use common keywords.
"""

from httpx import get, post
from pyfunctions import open_ai, open_ai_instruction, paragraph, verse, h2, h3, h4, image_from_url, headers, image_from_media
from time import sleep
import os
from dotenv import load_dotenv
load_dotenv()

pixabay_api_key = os.getenv('pixabay_api')

keywords = []
with open('keywords.txt', 'r+') as file:
    lines = file.readlines()
    for line in lines:
        key = line.strip()
        keywords.append(key)

for keyword in keywords:
    from random import choice
    wp_header = headers(os.getenv('wp_user'), os.getenv('wp_pass')) # change the password from the env file.

    info_kw = open_ai(f'write paragraph in 200 words about {keyword}')
    intro_content = open_ai_instruction(info_kw, 'improve readability')

    wp_content = paragraph(intro_content)

    # this section will choose random image from pixabay ##
    number = [1,2,3,4,5]
    random_image = choice(number)
    image_kw = keyword.replace(' ', '+')
    image_api = f'https://pixabay.com/api/?key={pixabay_api_key}&q={image_kw}&image_type=photo&per_page=10&min_width=900px'
    img_url = get(image_api).json().get('hits')[random_image].get('largeImageURL')

    # ## image download and uploading ##
    resp = get(f'{img_url}')
    with open(f'images/{keyword}.jpg', 'wb') as file:
        file.write(resp.content)
        features_img = image_from_media(f'images/{keyword}.jpg')

    media_upload_json = 'https://localhost/demosite/wp-json/wp/v2/media'
    res_id = post(media_upload_json, files=features_img, headers=wp_header, verify=False)
    feature_img_id = res_id.json().get('id')
    # print(feature_img_id)
    # end of image download and uploading #

    wp_content += image_from_url(img_url, keyword, f'{keyword} image')
    wp_content += h2(f'Different Types of {keyword}')

    different_types_product = open_ai(f'Write 100 words about different types of {keyword}')
    wp_content += paragraph(different_types_product)

    product_types = open_ai(f'list 2 types of {keyword}')
    products_list = product_types.strip().split('\n')

    wp_product_intro = []
    wp_product_feature = []
    wp_product_pros = []
    wp_product_cons = []
    wp_buying_guide = []

    sleep(60)

    for product in products_list:

        product_info = open_ai(f'{product}: write a 100 words info').strip()
        wp_product_intro.append(product_info)

        product_feature = open_ai(f'useful features of {product}').strip()
        wp_product_feature.append(product_feature)

        product_pros = open_ai(f'advantage of {product}, write in paragraph').strip()
        wp_product_pros.append(product_pros)

        product_cons = open_ai(f'disadvantage of {product}, write 120 words paragraph').strip()
        wp_product_cons.append(product_cons)

        buying_guide = open_ai(f'why buy {product}? write in 120 words paragraph').strip()
        wp_buying_guide.append(buying_guide)
        sleep(30)

    i = 0
    m = 1
    while i < len(products_list) or m < len(products_list):

        product_name = products_list[i]
        image_keyword = f'{product_name}'.replace(f'{m}. ', '')
        product_image_api = f'https://pixabay.com/api/?key={pixabay_api_key}&q={image_keyword}&image_type=photo'
        product_img_url = get(product_image_api).json().get('hits')[0].get('largeImageURL')

        product_info_with_image = paragraph(wp_product_intro[i])
        wp_content += h3(f'{products_list[i]}') + image_from_url(product_img_url, image_keyword, image_keyword) + product_info_with_image

        product_feature_text = verse(wp_product_feature[i])
        wp_content += h4('Features') + product_feature_text

        product_pros = paragraph(wp_product_pros[i])
        wp_content += h4('Advantages') + product_pros

        product_cons = paragraph(wp_product_pros[i])
        wp_content += h4('Disadvantage') + product_cons

        buying_guide = paragraph(wp_buying_guide[i])
        wp_content += h4('Should I Buy this') + buying_guide

        i += 1
        m += 1

    conclusion = h2('Final Thoughts') + paragraph(open_ai(f'Write a conclusion in 120 words about buying {keyword}'))
    wp_content += conclusion

    wp_title = f'{keyword} Buying Guide 2022'
    wp_slug = f'{wp_title}'.strip().replace(' ', '-')
    # wp_excerpt = open_ai_instruction(info_kw, 'make 30 words excerpt')

    # auto posting to WordPress
    wp_post_api = 'https://localhost/demosite/wp-json/wp/v2/posts'

    auto_posting = {
        'title': wp_title,
        'content': wp_content,
        'status': 'publish',
        'slug': wp_slug,
        'featured_media': feature_img_id,
        'categories': '255',
        # 'excerpt': wp_excerpt
    }
    res = post(wp_post_api, data=auto_posting, headers=wp_header, verify=False)
    print(f'{keyword} review articles posted on wordpress')

    sleep(600) # for the limitations of OpenAI, I have added delay of 5 minutes after every article.