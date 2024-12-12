def build_fancy_panel():
    filename = "fancy_panel.txt"

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
                    <tr class="bg-gray-100">
                        <td class="border px-4 py-2">China</td>
                        <td class="border px-4 py-2">1,411,778,724</td>
                    </tr>
                    <tr class="bg-white">
                        <td class="border px-4 py-2">India</td>
                        <td class="border px-4 py-2">1,393,409,038</td>
                    </tr>
                    <tr class="bg-gray-100">
                        <td class="border px-4 py-2">United States</td>
                        <td class="border px-4 py-2">332,915,073</td>
                    </tr>
                    <tr class="bg-white">
                        <td class="border px-4 py-2">Indonesia</td>
                        <td class="border px-4 py-2">276,361,783</td>
                    </tr>
                    <tr class="bg-gray-100">
                        <td class="border px-4 py-2">Pakistan</td>
                        <td class="border px-4 py-2">225,199,937</td>
                    </tr>
                    <tr class="bg-white">
                        <td class="border px-4 py-2">Brazil</td>
                        <td class="border px-4 py-2">213,993,437</td>
                    </tr>
                    <tr class="bg-gray-100">
                        <td class="border px-4 py-2">Nigeria</td>
                        <td class="border px-4 py-2">211,400,708</td>
                    </tr>
                    <tr class="bg-white">
                        <td class="border px-4 py-2">Bangladesh</td>
                        <td class="border px-4 py-2">166,303,498</td>
                    </tr>
                    <tr class="bg-gray-100">
                        <td class="border px-4 py-2">Russia</td>
                        <td class="border px-4 py-2">145,912,025</td>
                    </tr>
                    <tr class="bg-white">
                        <td class="border px-4 py-2">Mexico</td>
                        <td class="border px-4 py-2">130,262,216</td>
                    </tr>
                    
                </tbody>
            </table>
        </div>
    """

    data = {"filename": filename, "content": content}
    return data
