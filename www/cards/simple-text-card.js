class SimpleTextCard extends HTMLElement {
  setConfig(config) {
    if (!config.text) {
      throw new Error('You need to define some text');
    }
    this.config = config;
    this.innerHTML = config.text
    if (this.config.style) {
      this.style.cssText = this.config.style;
    }
  }

  getCardSize() {
    return 1;
  }
}

customElements.define("simple-text-card", SimpleTextCard);
console.info(`%cSIMPLE-TEXT-CARD 0.0.1 IS INSTALLED`, "color: green; font-weight: bold", "")
