"""
   Guttenberg Functions for WordPress are created by Sohanoor Rahman. An SEO Professional and Python Programmer. Love to code.
    Follow me on Github and others social medial:
        https://github.com/aboutsohan
        https://www.facebook.com/AboutSohan/
        https://twitter.com/AboutSohan
        https://www.linkedin.com/in/AboutSohan
        https://www.instagram.com/AboutSohan
"""

# Start of the TEXT Based Functions
# Total functions --- 14
def paragraph(text):
    """This functions will return paragraph codes into Gutenberg format for WordPress post.
    input: give any types of paragraph text"""

    wp_codes = f'<!-- wp:paragraph --><p>{text}</p><!-- /wp:paragraph -->'
    return wp_codes

def h2(heading):
    """This functions will return (heading 2) codes into Gutenberg format for WordPress post.
    input: give any types of heading text"""
    wp_codes = f'<!-- wp:heading --><h2>{heading}</h2><!-- /wp:heading -->'
    return wp_codes

def h3(heading):
    """This functions will return (heading 3) codes into Gutenberg format for WordPress post.
    input: give any types of heading text"""
    wp_codes = f'<!-- wp:heading {{"level":3}} --><h3>{heading}</h3><!-- /wp:heading -->'
    return wp_codes

def h4(heading):
    """This functions will return (heading 4) codes into Gutenberg format for WordPress post.
    input: give any types of heading text"""
    wp_codes = f'<!-- wp:heading {{"level":4}} --><h4>{heading}</h4><!-- /wp:heading -->'
    return wp_codes

def h5(heading):
    """This functions will return (heading 5) codes into Gutenberg format for WordPress post.
    input: give any types of heading text"""
    wp_codes = f'<!-- wp:heading {{"level":5}} --><h5>{heading}</h5><!-- /wp:heading -->'
    return wp_codes

def h6(heading):
    """This functions will return (heading 6) codes into Gutenberg format for WordPress post.
    input: give any types of heading text"""
    wp_codes = f'<!-- wp:heading {{"level":6}} --><h6>{heading}</h6><!-- /wp:heading -->'
    return wp_codes

def list_bullet(lists):
    """This functions will return (bullet list) codes into Gutenberg format for WordPress post.
    input: You have to input (python list)"""
    wp_codes = '<!-- wp:list --><ul>'
    for element in lists:
        wp_codes += f'<!-- wp:list-item --><li>{element}</li><!-- /wp:list-item -->'
    wp_codes += '</ul><!-- /wp:list -->'
    return wp_codes

def list_number(lists):
    """This functions will return (number list) codes into Gutenberg format for WordPress post.
        input: You have to input (python list)"""
    wp_codes = '<!-- wp:list {"ordered":true} --><ol>'
    for element in lists:
        wp_codes += f'<!-- wp:list-item --><li>{element}</li><!-- /wp:list-item -->'
    wp_codes += '</ol><!-- /wp:list -->'
    return wp_codes

def quote(text, citation):
    """This functions will return (quote & citation) codes into Gutenberg format for WordPress post.
        input: You have to input (text and citation)"""
    wp_codes = f'<!-- wp:quote --><blockquote class="wp-block-quote"><!-- wp:paragraph --><p>{text}</p>'
    wp_codes += f'<!-- /wp:paragraph --><cite>{citation}</cite></blockquote><!-- /wp:quote -->'
    return wp_codes

def codes(text):
    """This functions will return (wordpress codes) codes into Gutenberg format for WordPress post.
    input: You have to input (text)"""
    wp_codes = f'<!-- wp:code --><pre class="wp-block-code"><code>{text}</code></pre><!-- /wp:code -->'
    return wp_codes

def preformatted(text):
    """This functions will return (preformatted text) codes into Gutenberg format for WordPress post.
    input: You have to input (text)"""
    wp_codes = f'<!-- wp:preformatted --><pre class="wp-block-preformatted">{text}</pre><!-- /wp:preformatted -->'
    return wp_codes

def quote_pull(quote, citation):
    """This functions will return (pull quotation text) codes into Gutenberg format for WordPress post.
    input: You have to input (qutation text, citation src)"""
    wp_codes = f'<!-- wp:pullquote --><figure class="wp-block-pullquote"><blockquote><p>{quote}</p><cite>{citation}</cite></blockquote></figure><!-- /wp:pullquote -->'
    return wp_codes

def table(dicts):
    """This functions will return (tables) codes into Gutenberg format for WordPress post.
    input: You have to input (dictioanry)"""
    wp_codes = '<!-- wp:table --><figure class="wp-block-table"><table><tbody>'
    for key, value in dicts.items():
        wp_codes += f'<tr><td>{key}</td><td>{value}</td></tr>'
    wp_codes += '</tbody></table></figure><!-- /wp:table -->'
    return wp_codes

def verse(text):
    """This functions will return (verse) codes into Gutenberg format for WordPress post.
    input: You have to input (text)"""
    wp_codes = f'<!-- wp:verse --><pre class="wp-block-verse">{text}</pre><!-- /wp:verse -->'
    return wp_codes

## end of the TEXT blocks sections ##

# Start of the MEDIA Based Functions
# Total functions -- (23-14) = 9

def image_from_media(img_src):

    """This functions will return (image from folder) codes into Gutenberg format for WordPress post.
    input: You have to input (image source from folder)"""
    media_url = f'https://localhost/demosite/wp-json/wp/v2/media'
    files = {'file': open(img_src, 'rb')}
    return files

def image_from_url(img_src, alt, caption):
    """This functions will return (image from url) codes into Gutenberg format for WordPress post.
    input: You have to input (img_src, alt, caption)"""
    wp_code = f'<!-- wp:image {{"align":"center","sizeSlug":"large"}} --> <figure class="wp-block-image aligncenter size-large"><img src="{img_src}" alt="{alt}"/>'
    wp_code += f'<figcaption class="wp-element-caption">{caption}</figcaption></figure><!-- /wp:image -->'
    return wp_code

def image_id(id):
    """This function is not completed yet. we are working on this."""
    wp_codes = f'{id}'
    return wp_codes

def image_gallery():
    """This function is not completed yet. we are working on this."""
    wp_code = f''
    return wp_code

def audio():
    """This function is not completed yet. we are working on this."""
    wp_code = f''
    return wp_code

def cover():
    """This function is not completed yet. we are working on this."""
    wp_code = f''
    return wp_code

def file_download(id, img_src):
    """This functions will return (image download link from url) codes into Gutenberg format     for WordPress post.
        input: You have to input (file id, source url)"""
    wp_code = f'<!-- wp:file {{"id":{id},"href":"{img_src}"}} --><div class="wp-block-file"><a id="wp-block-file--media-5ee1ed20-d8e3-4b40-9acd-fd97e56d7551" href="{img_src}" target="_blank" rel="noreferrer noopener">flamingos-5</a><a href="{img_src}" class="wp-block-file__button wp-element-button" download aria-describedby="wp-block-file--media-5ee1ed20-d8e3-4b40-9acd-fd97e56d7551">Download</a></div><!-- /wp:file -->'
    return wp_code

def media_text(id, media_url, img_src, alt, content):
    """This functions will return (image & text) codes into Gutenberg format for WordPress post.
    input: You have to input (id, media_url, img_src, alt, content)"""
    wp_code = f'<!-- wp:media-text {{"mediaId":{id},"mediaLink":"{media_url}","mediaType":"image"}} -->'
    wp_code += f'<div class="wp-block-media-text alignwide is-stacked-on-mobile"><figure class="wp-block-media-text__media"><img src="{img_src}" alt="{alt}" class="wp-image-391 size-full"/></figure><div class="wp-block-media-text__content"><!-- wp:paragraph {{"placeholder":"Content…"}} --><p>{content}</p>'
    wp_code += '<!-- /wp:paragraph --></div></div><!-- /wp:media-text -->'
    return wp_code

def video_media(id, video_src, caption):
    """This functions will return (video media) codes into Gutenberg format for WordPress post.
    input: You have to input (video id, video_src, caption)"""
    wp_codes = f'<!-- wp:video {{"id":{id},"align":"center"}} --><figure class="wp-block-video aligncenter">'
    wp_codes += f'<video controls src="{video_src}"></video><figcaption class="wp-element-caption">{caption}</figcaption></figure><!-- /wp:video -->'
    return wp_codes

# End of the MEDIA Based Functions

# Start of the DESIGN Based Functions
# Total functions -- (25-23) = 2

def button():
    """This function is not completed yet. we are working on this."""
    wp_codes = ''
    return wp_codes

def spacer(pixel):
    """This functions will return (spacer) codes into Gutenberg format for WordPress post.
     input: You have to input (pixel number)"""
    wp_codes = f'<!-- wp:spacer {{"height":"{pixel}px"}} --><div style="height:{pixel}px" aria-hidden="true" class="wp-block-spacer"></div><!-- /wp:spacer -->'
    return wp_codes

# End of the DESIGN Based Functions

# Start of the WIDGETS Based Functions
# Total functions -- (26-25) = 1

def html_code(code):
    """This functions will return (custom html widget) codes into Gutenberg format for WordPress post.
    input: You have to input (html codes)"""
    wp_codes = f'<!-- wp:html -->{code}<!-- /wp:html -->'
    return wp_codes

# End of the WIDGETS Based Functions

# Start of the EMBED Based Functions
# Total functions -- (27-26) = 1

def youtube(yt_src):
    """This functions will return (Youtube embled widget) codes into Gutenberg format for WordPress post.
    input: You have to input (Youtube video URL)"""
    wp_codes = f'<!-- wp:embed {{"url":"{yt_src}","type":"video","providerNameSlug":"youtube","responsive":true,"align":"center","className":"wp-embed-aspect-16-9 wp-has-aspect-ratio"}} --><figure class="wp-block-embed aligncenter is-type-video is-provider-youtube wp-block-embed-youtube wp-embed-aspect-16-9 wp-has-aspect-ratio"><div class="wp-block-embed__wrapper">{yt_src}</div></figure><!-- /wp:embed -->'
    return wp_codes

# End of the EMBLED Based Functions

# WordPress Headers Functions for AutoPosting
def headers(wp_user, wp_pass):
    """This functions will return (wp headers) for WordPress.
    input: You have to input (username & password)"""
    import base64
    wp_credential = f'{wp_user}:{wp_pass}'
    wp_token = base64.b64encode(wp_credential.encode())
    wp_header = {'Authorization': f'Basic {wp_token.decode("utf-8")}'}
    return wp_header

# OpenAI Functions content generator
def open_ai(prompt):
    """This functions will return (OpenAI) output contents.
    input: You have to input (instruction)"""
    import os
    from dotenv import load_dotenv
    load_dotenv()
    import openai

    openai.api_key = os.getenv('API_KEY')

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=1,
        max_tokens=1000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    data =  response.get('choices')[0].get('text')
    return data

content = open_ai('List 3 freedom fighters of bangladesh')

# OpenAI Functions to give instruction the content
def open_ai_instruction(input, instruction):
    """This functions will return (Updated Content).
    input: You have to input (content source and instructions to modify content.)"""
    import os
    from dotenv import load_dotenv
    load_dotenv()
    import openai

    openai.api_key = os.getenv("API_KEY")

    response = openai.Edit.create(
        model="text-davinci-edit-001",
        input=input,
        instruction=instruction,
        temperature=1,
        top_p=1
    )
    data = response.get('choices')[0].get('text')
    return data