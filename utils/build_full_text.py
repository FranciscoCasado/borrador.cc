import os
import frontmatter

rootdir = "../content/comisiones"
with open ("../content/texto-completo.md","w") as full_text:
    full_text.write("---\n")
    full_text.write(f"title: \"Texto Completo\"\n")
    full_text.write(f"weight: 0\n")
    full_text.write("bookHidden: true\n")
    full_text.write("---\n")
    
    for entry in sorted(os.listdir(rootdir)):
        comision_path = os.path.join(rootdir, entry)
        if os.path.isdir(comision_path):
            comision = frontmatter.load(comision_path + "/_index.md")
            full_text.write("## " + comision["title"] + "\n")
            full_text.write("**" + comision["long-title"] + "**\n")
            if comision["ready"]:
                full_text.write("\n*" + comision["status"] + "*\n")
            else:
                full_text.write("{{< hint warning >}} \n &#9432 " + comision["status"] + "{{< /hint >}}\n")
                
            full_text.write("\n")
            
            if os.path.exists(comision_path + "/articulos"):
                for file in sorted(os.listdir(comision_path + "/articulos")):
                    article_path = os.path.join(comision_path + "/articulos", file)
                    article = frontmatter.load(article_path)
                    
                    full_text.write("### " + article["title"] + "\n")
                    full_text.write(article.content)
                    full_text.write("\n\n")
                    
            full_text.write("\n")
            