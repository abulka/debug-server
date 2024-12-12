import json

def build_fancy_panel(json_string):
    data = json.loads(json_string)
    
    content = """
        <div class="max-w-4xl mx-auto">
            <table class="table-auto bg-white shadow-md rounded my-6 w-full">
                <thead>
                    <tr class="bg-blue-500 text-white">
                        <th class="px-4 py-2">Country</th>
                        <th class="px-4 py-2">Population</th>
                    </tr>
                </thead>
                <tbody>
    """
    
    for i, entry in enumerate(data):
        row_class = "bg-gray-100" if i % 2 == 0 else "bg-white"
        content += f"""
                    <tr class="{row_class}">
                        <td class="border px-4 py-2">{entry['country']}</td>
                        <td class="border px-4 py-2">{entry['population']}</td>
                    </tr>
        """
    
    content += """
                </tbody>
            </table>
        </div>
    """
    
    # return {"filename": "fancy_panel.txt", "content": content}
    return content

example_table_json_string = json.dumps([
    {"country": "China", "population": "1,411,778,724"},
    {"country": "India", "population": "1,393,409,038"},
    {"country": "United States", "population": "332,915,073"},
    {"country": "Indonesia", "population": "276,361,783"},
    {"country": "Pakistan", "population": "225,199,937"},
    {"country": "Brazil", "population": "213,993,437"},
    {"country": "Nigeria", "population": "211,400,708"},
    {"country": "Bangladesh", "population": "166,303,498"},
    {"country": "Russia", "population": "145,912,025"},
    {"country": "Mexico", "population": "130,262,216"},
    {"country": "Japan", "population": "125,584,838"},
    {"country": "Ethiopia", "population": "117,876,227"},
    {"country": "Philippines", "population": "113,804,629"},
    {"country": "Egypt", "population": "104,258,327"},
    {"country": "Vietnam", "population": "98,168,833"},
    {"country": "DR Congo", "population": "89,561,403"},
    {"country": "Turkey", "population": "84,339,067"},
    {"country": "Iran", "population": "85,028,759"},
    {"country": "Germany", "population": "83,900,473"},
    {"country": "Thailand", "population": "69,950,850"},
])
