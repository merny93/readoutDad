import os, io, sys



##build up the html files from resources



def read_css(css_file_path):
    try:
        with open(css_file_path) as f_obj:
            css = f_obj.read()
    except Exception as error:
        print("Error opening .css file.")
        print(error, type(error))
    else:
        return css

def read_js(js_file_path):
    try:
        with open(js_file_path) as f_obj:
            js = f_obj.read()
    except Exception as error:
        print("Error opening .js file.")
        print(error, type(error))
    else:
        return js

def build_html():
    html_dir = os.path.join(os.path.dirname(__file__), '..', 'frontend', 'html')
    html_files = os.listdir(html_dir)
    gui_dir = os.path.join(os.path.dirname(__file__), '..', '..','gui')
    for html_file in html_files:
        html_file_path = os.path.join(html_dir,html_file)
        html=''
        with open(html_file_path) as f_obj:
            lines = f_obj.readlines()
            for line in lines:
                if '<link' in line:
                    link_parts = line.split(' ')
                    for part in link_parts:
                        if 'href' in part:
                            if 'http' in part:
                                html+= line
                            else:
                                css_file_path = part.replace('href="', '').replace('">', '').replace('"', '').replace('\n', '')
                                css_file_path = os.path.join(html_dir, css_file_path)
                                css = read_css(css_file_path)
                                html += '<style>\n'
                                html += css
                                html += '</style>\n'                    
                            
                elif '<script' in line:
                    if 'src' in line:
                        script_parts = line.split(' ')
                        for part in script_parts:
                            if 'src' in part:
                                if 'http' in part:
                                    html+= line
                                else:
                                    js_file_path = part.replace('src="', '').replace('"></script>', '').replace('"', '').replace('\n', '')
                                    js_file_path = os.path.join(html_dir, js_file_path)
                                    js = read_js(js_file_path)
                                    html += '<script>\n'
                                    html += js
                                    html += '</script>\n'                        
                    else:
                        html+= line
                else:
                    html+= line
                
        file_save = open(os.path.join(gui_dir,html_file ), 'w')
        file_save.write(html)
        file_save.close()
    return True
                    
if __name__ == '__main__':
    if build_html():
        print('Built with successsss')
    else:
        print('built without successsss')