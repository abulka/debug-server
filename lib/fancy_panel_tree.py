def build_fancy_panel_tree(json_data):
    def create_tree_html(node, level=0):
        html = f'<div class="ml-{level * 4}">\n'

        # Only add the icon if the node has children
        if "children" in node and node["children"]:
            html += f'<p class="font-bold cursor-pointer" onclick="toggleCollapse(this)">\n'
            html += f'▶ {node["name"]}</p>\n'  # Remove span with .icon class
            html += '<div class="ml-4 hidden">'  # Hide child elements by default
            for child in node["children"]:
                html += create_tree_html(child, level + 1)
            html += '</div>'
        else:
            # For leaf nodes without children, don't add an icon
            html += f'<p class="font-bold">{node["name"]}</p>\n'

        html += '</div>'
        return html

    filename = "fancy_panel_tree.txt"
    content = f"""
    <style>
        p.font-bold.cursor-pointer {{
          position: relative;
          padding-left: 1.5em;
        }}
        p.font-bold.cursor-pointer::before {{
          content: "▶";
          position: absolute;
          left: 0;
          transition: transform 0.2s ease;
        }}
        p.font-bold.cursor-pointer.expanded::before {{
          content: "▼";
          transform: rotate(90deg);
        }}
    </style>
    <script>
        function toggleCollapse(element) {{
            var content = element.nextElementSibling;
            if (content) {{
                content.classList.toggle('hidden');
                element.classList.toggle('expanded');
            }}
        }}
        // Expand all nodes by default
        window.onload = function() {{
            var nodes = document.querySelectorAll('p.font-bold.cursor-pointer');
            nodes.forEach(function(node) {{
                var content = node.nextElementSibling;
                if (content) {{
                    node.classList.add('expanded');
                    content.classList.remove('hidden');
                }}
            }});
        }};
    </script>
    <div class="max-w-4xl mx-auto">
        {create_tree_html(json_data)}
    </div>
    """

    print(content)
    
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
