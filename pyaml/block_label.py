
# def block_label(label):
#     return \
# f"""type: markdown
# style: |
#   ha-card {{background: none; box-shadow: none; color: #BBB;
#     position: relative; top: 20px; left: -15px;}}
# content: |
#   ## {label}
#     """
def block_label(label):
    return \
f"""type: custom:simple-text-card
text: {label}
style: |
  color: #CCC; font-size: 24px; margin-top: 28px;
"""
