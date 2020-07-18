def scene_button(name, entity):
    return f"""type: "custom:button-card"
name: {name}
icon: mdi:lightbulb-group
entity: {entity}
aspect_ratio: 1/1
show_state: false
styles:
  card:
    - border-radius: 12px
    - background: #ececec
    - opacity: 0.65
  icon:
    - color: gray
  grid:
    - grid-template-areas: '"i" "n"'
    - grid-template-columns: 1fr
    - grid-template-rows: 2fr 1fr
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
