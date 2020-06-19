def tag(tag, *args, **kwargs):
    if 'html_class' in kwargs:
        kwargs["class"] = kwargs.pop('html_class')
    attrs = ''.join(f'{k} = "{v}"' for k, v in kwargs.items())
    inner = ''.join(args)
    return f'<{tag} {attrs}>{inner}</{tag}>'


if __name__ == '__main__':
    print(
        tag('p',
            tag('span', 'Curso de Python 3, por'),
            tag('strong', 'Danilo Simões', id='ds'),
            tag('span', 'e'),
            tag('strong', 'Edna Izabel', id='ei'),
            tag('span', '.'),
            html_class="alert")

    )
