def scene_button(name, entity):
    return f"""type: "custom:button-card"
name: {name}
entity: {entity}
aspect_ratio: 1/1
show_state: true
styles:
  card:
    - border-radius: 12px
    - background: #ececec
    - opacity: 0.6
  name:
    - justify-self: start
    - padding-left: 6%
  state:
    - font-size: .75em
    - color: transparent
  icon:
    - color: gray
tap_action:
  action: call-service
  service: scene.turn_on
  service_data:
    entity_id: {entity}
double_tap_action:
  action: call-service
  service: upb.link_deactivate
  service_data:
    entity_id: {entity}
"""
