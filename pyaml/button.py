#
# Template to define a custom button with Homekit-type styling
#

import re
from svg import svg

def homekit_button(name, entity, icon=None, tap=True, double_tap=True):
    tap_action  = "tap_action:\n  action: toggle\n  haptic: light" if tap else ""
    double_tap_action = _popup_action(name) if double_tap else ""

    return f"""type: "custom:button-card" 
name: {name}
entity: {entity}
aspect_ratio: 1/1
show_icon: false
show_state: false
extra_styles: >
  svg path.transition {{transition: fill 1.2s ease;}}
{tap_action}
{double_tap_action}
{_homekit_style()}
{_custom_fields(icon)}
{_state_styles()}
hold_action:
  action: more-info
  haptic: success
"""


def _state_styles():
    return """state:
  - {"value": "on", "styles": {"card": [{"opacity": "1.0"}]}}
  - {"value": "off", "styles": {"card": [{"opacity": ".65"}]}}
  - {"value": "unavailable", "styles": {"card": [{"opacity": ".65"}]}}
    """

def _homekit_style():
    return f"""styles:
  card:
    - border-radius: 12px
    - background: #ececec
  grid:
    - grid-template-areas: '"i" "n"'
    - grid-template-columns: 1fr
    - grid-template-rows: 2fr 1fr
  custom_fields:
    svg_icon:
      [top: 11%, left: 4%, width: 44%, position: absolute]
    info:
      [top: 8.5%, right: 4%, width: 44%, position: absolute]
"""

def _custom_fields(icon):
    svg_icon_str = f"{svg(icon)}" if icon else f"{svg('icons/default.svg')}"
    return f"""custom_fields:
  svg_icon: >
    [[[return `{svg_icon_str}`;]]]
  info: >
    [[[{circle_brightness()}]]]
"""


def _popup_action(name):
    return f"""double_tap_action:
  action: call-service
  service: browser_mod.popup
  service_data:
    title: {name}
    deviceID: this
    card:
      type: entities
      show_header_toggle: false
      style: 'ha-card {{border-radius: 0em; background: #686868;}}'
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
            #popup {{margin: -2.4em 0 .4em 0;}}
            #popup > div.range-holder > input[type=range] {{cursor: grab;}}
            #popup h4 {{margin-bottom: .7em; color: #ccc;
              font-size: 2em; font-weight: 400;}}
"""


def circle_brightness():
    return re.sub(r"\n\s*", " ", """
      let brightness = 0;
      let text = "";
      if ("brightness" in entity.attributes) {
        brightness = Math.round(entity.attributes.brightness / 2.54);
        text = brightness + '%';
      } else if (entity.state == 'on') {
        brightness = 100;
        text = 'On';
      } else {
        text = 'Off'
      }
      const radius = entity.attributes.dimmable ? 20.5 : 0;
      const circumference = radius * 2 * Math.PI;
      return
        `<svg viewBox="0 0 50 50">
          <circle cx="25" cy="25" r="${radius}" stroke="#d8d8d8"
            stroke-width="0.75" fill="none";/>
          <circle cx="25" cy="25" r="${radius}" stroke="#999"
            stroke-width="1.75" fill="none"
            style="transform: rotate(-90deg); transform-origin: 50% 50%;
            stroke-dasharray: ${circumference};
            stroke-dashoffset: ${circumference-brightness/100*circumference};"/>
          <text x="25" y="26" fill="#999" font-size="14"
             text-anchor="middle" dominant-baseline="middle">${text}</text>
        </svg>`;
    """)
