#
# Template to define a custom button with Homekit-type styling
#

from svg import svg

def homekit_light_button(name, entity, icon=None):
    icon_str = f"icon: {icon}" if icon else ""
    return \
f"""type: "custom:button-card" 
name: {name}
entity: {entity}
aspect_ratio: 1/1
show_icon: false
show_state: true
extra_styles: >
  svg path.transition {{transition: fill 1.2s ease;}}

tap_action:
  action: toggle
  haptic: light

hold_action:
  action: more-info
  haptic: success

{_homekit_style()}

{_custom_fields(icon)}

state:
  - value: "on"
    styles:
      card:
        - opacity: 1.0
      state:
        - color: gray
  - value: "off"
    styles:
      card:
        - opacity: 0.6
      icon:
        - color: gray
      state:
        - color: gray
  - value: "unavailable"
    styles:
      card:
        - opacity: 0.6
      icon:
        - color: black
    """


def _homekit_style():
    return \
        f"""
styles:
  card:
    - border-radius: 12px
    - background: #ececec
  name:
    - justify-self: start
    - padding-left: 6%
  state:
    - font-size: .75em
    - text-transform: capitalize
    - justify-self: start
    - padding-left: 6%
  grid:
    - grid-template-rows: 1fr min-content min-content min-content
  custom_fields:
    svg_icon:
      [top: 11%, left: 4%, width: 44%, position: absolute]
    info:
      [top: 8.5%, right: 4%, width: 44%, position: absolute]
        """

def _custom_fields(icon):
    svg_icon_str = f"svg_icon: {svg(icon)}" if icon else f"svg_icon: {svg('icons/pendant.svg')}"
    return \
        f"""
custom_fields:
  {svg_icon_str}
  info: >
    [[[if (entity.state === 'on' && entity.attributes.brightness) {{
      const brightness = Math.round(entity.attributes.brightness / 2.54);
      const radius = 20.5; const circumference = radius * 2 * Math.PI; 
      return `<svg viewBox="0 0 50 50"><circle cx="25" cy="25" r="${{radius}}" stroke="#b2b2b2" stroke-width="1.5" fill="none" style="
      transform: rotate(-90deg); transform-origin: 50% 50%; stroke-dasharray: ${{circumference}}; stroke-dashoffset: ${{circumference - brightness / 100 * circumference}};" />
      <text x="50%" y="60%" fill="#8d8e90" font-size="14" text-anchor="middle" alignment-baseline="middle">${{brightness}}<tspan font-size="10">%</tspan></text></svg>`; }}
    ]]]
        """
