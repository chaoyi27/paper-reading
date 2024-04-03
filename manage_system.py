# 论文信息管理系统

def add_paper_with_image(title, authors, institutions, tags, abstract, link, notes, image_path=None, filename="data/papers.md"):
    """
    向Markdown文件添加一篇论文记录，包括图片。
    """
    with open(filename, "a", encoding="utf-8") as file:
        # 论文标题和作者
        file.write(f"# {title}\n\n")
        file.write(f"- **作者**: {', '.join(authors)}\n")
        file.write(f"- **机构**: {', '.join(institutions)}\n")
        
        # 标签
        formatted_tags = ', '.join([f"`{tag}`" for tag in tags])
        file.write(f"- **标签**: {formatted_tags}\n\n")
        
        # 图片
        if image_path:
            file.write(f"![Teaser Image]({image_path})\n\n")
        
        # 摘要
        file.write(f"## 摘要\n\n{abstract}\n\n")
        
        # 链接
        file.write(f"## 链接\n\n[论文PDF]({link})\n\n")
        
        # 个人注释
        file.write(f"## 注释\n\n{notes}\n\n")


def add_paper(title, authors, institutions, tags, abstract, link, notes, filename="data/papers.md"):
    """
    向Markdown文件添加一篇论文记录。
    """
    with open(filename, "a", encoding="utf-8") as file:
        # 论文标题和作者
        file.write(f"# {title}\n\n")
        file.write(f"- **作者**: {', '.join(authors)}\n")
        file.write(f"- **机构**: {', '.join(institutions)}\n")
        
        # 标签
        formatted_tags = ', '.join([f"`{tag}`" for tag in tags])
        file.write(f"- **标签**: {formatted_tags}\n\n")
        
        # 摘要
        file.write(f"## 摘要\n\n{abstract}\n\n")
        
        # 链接
        file.write(f"## 链接\n\n[论文PDF]({link})\n\n")
        
        # 个人注释
        file.write(f"## 注释\n\n{notes}\n\n")


def add_tag(tag, description, filename="data/tags.txt"):
    """
    向标签文件添加一个新的标签。
    """
    with open(filename, "a", encoding="utf-8") as file:
        file.write(f"{tag}: {description}\n")


def add_institution(name, abbreviation, filename="data/institutions.txt"):
    """
    向机构文件添加一个新的机构。
    """
    with open(filename, "a", encoding="utf-8") as file:
        file.write(f"{abbreviation}: {name}\n")


# 示例使用
if __name__ == "__main__":
    # 添加一篇论文记录
    add_paper(
        title="示例论文标题",
        authors=["作者1", "作者2"],
        institutions=["机构1", "机构2"],
        tags=["nav", "sim2real"],
        abstract="这里是摘要",
        link="http://example.com",
        notes="这里是注释"
    )
    
    add_paper_with_image(
    title="示例论文标题",
    authors=["作者1", "作者2"],
    institutions=["机构1", "机构2"],
    tags=["nav", "sim2real"],
    abstract="这里是摘要",
    link="http://example.com",
    notes="这里是注释",
    image_path="http://example.com/teaser.jpg"  # 或本地路径 "./images/teaser.jpg"
    )


    # 添加标签
    add_tag("nav", "导航")
    add_tag("sim2real", "从仿真到现实")

    # 添加机构
    add_institution("北京大学", "PKU")
    add_institution("慕尼黑技术大学", "TUM")
