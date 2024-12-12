def build_fancy_panel_tree(json_data):
    def create_tree_html(node, level=0):
        html = f'<div class="ml-{level * 4}">\n'
        html += f'<p class="font-bold cursor-pointer" onclick="toggleCollapse(this)">\n'
        if "children" in node and node["children"]:
            html += f'<span class="icon collapsed">▼</span> '
        html += f'{node["name"]}</p>\n'
        if "children" in node:
            html += '<div class="ml-4 hidden">'  # Hide child elements by default
            for child in node["children"]:
                html += create_tree_html(child, level + 1)
            html += '</div>'
        html += '</div>'
        return html

    filename = "fancy_panel_tree.txt"
    content = f"""
    <style>
        .icon::before {{ content: "▼"; display: inline-block; width: 1em; }}
        .icon.collapsed::before {{ content: "▶"; }}
        .hidden {{ display: none; }}  /* Hide child elements by default */
    </style>
    <script>
        function toggleCollapse(element) {{
            var content = element.nextElementSibling;
            if (content) {{
                content.classList.toggle('hidden');
                element.querySelector('.icon').classList.toggle('collapsed');
            }}
        }}
        // Expand all nodes by default
        window.onload = function() {{
            var nodes = document.querySelectorAll('.icon');
            nodes.forEach(function(node) {{
                node.classList.remove('collapsed');
                node.parentNode.nextElementSibling.classList.remove('hidden');
            }});
        }};
    </script>
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
                        {"name": "Leaf 1-1-2"},
                        {"name": "Leaf 1-1-3"}
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
                {
                    "name": "Leaf 2-1",
                    "children": [
                        {"name": "Leaf 2-1-1"},
                        {"name": "Leaf 2-1-2"}
                    ]
                },
                {"name": "Leaf 2-2"}
            ]
        },
        {
            "name": "Branch 3",
            "children": [
                {
                    "name": "Leaf 3-1",
                    "children": [
                        {"name": "Leaf 3-1-1"},
                        {"name": "Leaf 3-1-2"},
                        {"name": "Leaf 3-1-3"}
                    ]
                }
            ]
        },
        {
            "name": "Branch 4",
            "children": [
                {"name": "Leaf 4-1"},
                {"name": "Leaf 4-2"},
                {"name": "Leaf 4-3"},
                {
                    "name": "Leaf 4-4",
                    "children": [
                        {"name": "Leaf 4-4-1"},
                        {"name": "Leaf 4-4-2"}
                    ]
                }
            ]
        },
        {
            "name": "Branch 5",
            "children": [
                {"name": "Leaf 5-1"},
                {
                    "name": "Leaf 5-2",
                    "children": [
                        {"name": "Leaf 5-2-1"},
                        {"name": "Leaf 5-2-2"}
                    ]
                }
            ]
        }
    ]
}
