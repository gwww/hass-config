#
# Template to define a custom button with Homekit-type styling
#

from svg import svg

def homekit_light_button(name, entity, icon=None, tap=True, double_tap=True):
    icon_str = f"icon: {icon}" if icon else ""
    tap_action  = "tap_action:\n  action: toggle\n  haptic: light" if tap else ""
    double_tap_action = _popup_action(name) if double_tap else ""

    return f"""
type: "custom:button-card" 
name: {name}
entity: {entity}
aspect_ratio: 1/1
show_icon: false
show_state: true
extra_styles: >
  svg path.transition {{transition: fill 1.2s ease;}}

{tap_action}

hold_action:
  action: more-info
  haptic: success

{double_tap_action}

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
    return f"""
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
    return f"""
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


def _popup_action(name):
    return f"""
double_tap_action:
  action: call-service
  service: browser_mod.popup
  service_data:
    title: {name}
    deviceID: this
    autoclose_popup_card: 5000
    style:
      --ha-card-border-radius: 1em
      --more-info-header-color: rgba(255,255,255,1)
      background: none
      box-shadow: none
    card:
      type: vertical-stack
      cards:
        - type: entities
          show_header_toggle: false
          style: >
            ha-card {{animation: pop-in 0.8s 
              cubic-bezier(0.16, 1, 0.3, 1) both; transform-origin: center;
              border-radius: 1em; padding: 0.3em 1.25em 0.4em 0.5em; 
              box-shadow: none;
              background: linear-gradient(180deg, rgba(48,52,52,1) 0%,
              rgba(48,52,52,1) 4.8em, rgba(34,38,39,1) 4.8em,
              rgba(34,38,39,1) 100%); }}
            .card-header {{margin: -0.4em 0 1.4em 0.4em;
              font-family: sf text; letter-spacing: 0.005em;
              font-size: 1.5em;}}
            @keyframes pop-in {{0% {{transform: scale(0.6); opacity: 0;}}
              20% {{ opacity: 0; }} 100% {{transform: scale(1); opacity: 0.9;}}}}
          entities:
            - type: custom:light-popup-card
              entity: '[[[ return entity.entity_id ]]]'
              icon: none
              fullscreen: false
              brightnessWidth: 130px
              brightnessHeight: 360px
              borderRadius: 1.7em
              sliderColor: '#c7c7c7'
              sliderTrackColor: rgba(25, 25, 25, 0.9)
              actionSize: 4.5em
              actionsInARow: 2
              style: >
                #popup {{margin: -2.4em 0 1.4em 0;}}
                #popup > div.range-holder > input[type=range] {{cursor: grab;}}
                #brightnessValue {{color: rgba(255, 255, 255, 0.8); 
                  margin: -1em 0 0 0; font-size: 2em; font-weight: 400; 
                  position: absolute; z-index: 100;
                  font-family: SF Display, sans-serif;
                  letter-spacing: 0.02em; pointer-events: none; 
                  mix-blend-mode: difference; text-align:center; 
                  width: 3.4em; height: 3.4em; }}
                #popup > div.range-holder > input[type=range]::-webkit-slider-thumb
                  {{border: 0; eight: 0; width: 0; cursor: grabbing;}}
                #popup > div.action-holder > div > div
                  {{margin: 0.8em 0.5em -0.8em 0.5em;}}
                #popup > div.action-holder > div:nth-child(2) > div:nth-child(2) > span
                  {{background: radial-gradient(circle, rgba(255,255,255,1) 0%, rgba(255,255,255,0) 80%), 
                  conic-gradient(rgb(120,39,230), rgb(230,34,231), rgb(228,5,136), rgb(228,25,25), rgb(229,105,30), rgb(232,226,46), 
                  rgb(125,230,41), rgb(52,232,40), rgb(51,231,92), rgb(52,232,224),rgb(32,125,229), rgb(18,39,229), rgb(120,39,230));
                  border-width: 2px; border-color: #e6e6e6; --size: 4.4em !important; }}
"""
