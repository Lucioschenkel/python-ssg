class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        html_props = ""
        if self.props is None:
            return html_props

        for attr, val in self.props.items():
            html_props += f" {attr}=\"{val}\""
        return html_props

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError('All leaf nodes must have a value')

        if self.tag is None:
            return self.value

        html_props = self.props_to_html()
        return f"<{self.tag}{html_props}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if self.tag is None:
            raise ValueError('no tag specified')

        if self.children is None:
            raise ValueError('no children specified')

        output = ""
        for child in self.children:
            output += child.to_html()

        props = self.props_to_html()
        return f"<{self.tag}{props}>{output}</{self.tag}>"
