class Test1:
    def test_1(self, sb):
        sb.wait(1)
        sb.assert_text("PRODUCTS", "span.title")

    def test_2(self, sb):
        sb.wait(1)
        sb.assert_element("div.inventory_list")


class Test2:
    def test_3(self, sb):
        sb.wait(1)
        sb.assert_text("PRODUCTS", "span.title")

    def test_24(self, sb):
        sb.wait(1)
        sb.assert_element("div.inventory_list")
