import os

def write_highlighted_html(html, out_dir, example_idx):
    '''Adds some styles to HTML and writes to file'''
    html = '''
    
<!DOCTYPE html>
<html>
<head>
<style>
span {
  font-family:helvetica;
}
</style>
</head>
<body>

<button id="btnPrev" class="float-left submit-button" >Prev</button>
<button id="btnNext" class="float-left submit-button" >Next</button>
<span>(You may also use the left and right arrow keys)</span>
<br><br>

<span>The designated <b>summary</b> sentence was created by <b>fusing</b> the two designated <b>article</b> sentences together. 
The highlighted spans of a single color (e.g. blue) represent a <b>Point of Correspondence</b>. 
There may be multiple Points of Correspondence. Each Point of Correspondence also has a <b>type</b>, which can be one of the following: {Nominal, Pronominal, Common-Noun, Repetition, Event}. </span>

<script type="text/javascript">
    document.getElementById("btnPrev").onclick = function () {
        location.href = "%06d_highlighted.html";
    };
    document.getElementById("btnNext").onclick = function () {
        location.href = "%06d_highlighted.html";
    };

    document.addEventListener("keyup",function(e){
   var key = e.which||e.keyCode;
   switch(key){
      //left arrow
      case 37:
         document.getElementById("btnPrev").click();
      break;
      //right arrow
      case 39:
         document.getElementById("btnNext").click();
      break;
   }
});
</script>

''' % (example_idx - 1, example_idx + 1) + html
    html += '''
</body>
</html>
'''
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)
    path = os.path.join(out_dir, '%06d_highlighted.html' % example_idx)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)


# Colors to be used for each Point of Correspondence
highlight_colors = ['aqua', 'lime', 'yellow', '#FF7676', '#B9968D', '#D7BDE2', '#8C8DFF', '#D6DBDF', '#F852AF', '#00FF8B', '#FD933A', '#965DFF']


def start_tag_highlight(color):
    return "<span style='background-color: " + color + ";'>"


def html_highlight_poc(summary_sent_tokens, article_sent_tokens, sent1_idx, sent2_idx, fused_sent_idx, pocs):
    '''Creates the HTML with highlight Points of Correspondence'''
    end_tag = "</span>"
    out_str = ''

    # Display the Point of Correspondence types
    out_str += '<h1 style="font-family:helvetica;">Points of Correspondence</h1>'
    poc_types = [poc['PoC_Type'] for poc in pocs]
    for idx, poc_type in enumerate(poc_types):
        color = highlight_colors[idx]
        start_tag = start_tag_highlight(color)
        insert_string = start_tag + poc_type + end_tag + '<br>'
        out_str += insert_string
    if len(poc_types) == 0:
        out_str += '<span>[no points of correspondences found]</span><br>'
    out_str += '<br>'

    # Display the Summary sentences
    out_str += '<h1 style="font-family:helvetica;">Summary</h1>'
    for summ_sent_idx, summ_sent in enumerate(summary_sent_tokens):
        if fused_sent_idx == summ_sent_idx:
            out_str += '<div style="border:3px; border-style:solid; border-color:#FF0000; padding: 0.5em;">'
        else:
            out_str == '<div>'
        for token_idx, token in enumerate(summ_sent):
            color = 'white'
            if summ_sent_idx == fused_sent_idx:
                for poc_idx, poc in enumerate(pocs):
                    if token_idx >= poc['Sentence_Fused_Selection'][0] and token_idx < poc['Sentence_Fused_Selection'][1]:
                        color = highlight_colors[poc_idx]
            start_tag = start_tag_highlight(color)
            insert_string = start_tag + token + ' ' + end_tag
            out_str += insert_string
        out_str += '</div>'
        out_str += '<br>'
        if fused_sent_idx != summ_sent_idx:
            out_str += '<br>'

    # Display the Article sentences
    out_str += '<h1 style="font-family:helvetica;">Article</h1>'
    for article_sent_idx, sent in enumerate(article_sent_tokens):
        if article_sent_idx  == sent1_idx or article_sent_idx == sent2_idx:
            out_str += '<div style="border:3px; border-style:solid; border-color:#FF0000; padding: 0.25em;">'
        else:
            out_str == '<div>'
        source_sentence = article_sent_tokens[article_sent_idx]
        out_str += "<p style='margin:5px'>"
        for token_idx, token in enumerate(source_sentence):
            color = 'white'
            if article_sent_idx == sent1_idx:
                for poc_idx, poc in enumerate(pocs):
                    if token_idx >= poc['Sentence_1_Selection'][0] and token_idx < poc['Sentence_1_Selection'][1]:
                        color = highlight_colors[poc_idx]
            elif article_sent_idx == sent2_idx:
                for poc_idx, poc in enumerate(pocs):
                    if token_idx >= poc['Sentence_2_Selection'][0] and token_idx < poc['Sentence_2_Selection'][1]:
                        color = highlight_colors[poc_idx]
            start_tag = start_tag_highlight(color)
            insert_string = start_tag + token + ' ' + end_tag
            out_str += insert_string
        out_str += "</p>"
        out_str += '</div>'
    out_str += '<br>------------------------------------------------------<br><br>'
    return out_str
















