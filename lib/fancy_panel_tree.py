def build_fancy_panel_tree(json_data):
    def create_tree_html(node, level=0):
        html = f'<div class="ml-{level * 4}">'
        html += f'<p class="font-bold">{node["name"]}</p>'
        if "children" in node:
            for child in node["children"]:
                html += create_tree_html(child, level + 1)
        html += '</div>'
        return html
    
    filename = "fancy_panel_tree.txt"
    content = f"""
        <div class="max-w-4xl mx-auto">
            {create_tree_html(json_data)}
        </div>
    """
    
    data = {"filename": filename, "content": content}
    return data


example_json_data = {
    "name": "Root",
    "children": [
        {
            "name": "Branch 1",
            "children": [
                {
                    "name": "Leaf 1-1",
                    "children": [
                        {"name": "Leaf 1-1-1"},
                        {"name": "Leaf 1-1-2"}
                    ]
                },
                {
                    "name": "Leaf 1-2",
                    "children": [
                        {"name": "Leaf 1-2-1"},
                        {"name": "Leaf 1-2-2"}
                    ]
                }
            ]
        },
        {
            "name": "Branch 2",
            "children": [
                {"name": "Leaf 2-1"},
                {"name": "Leaf 2-2"}
            ]
        },
        {
            "name": "Branch 3",
            "children": [
                {"name": "Leaf 3-1"}
            ]
        }
    ]
}