import esphome
import esphome.config_validation as cv
import esphome.codegen as cg
from esphome.components import display, spi
from esphome.const import CONF_ID, CONF_LAMBDA

CODEOWNERS = ["@your_username"]
DEPENDENCIES = ["spi"]

gdep073e01_ns = cg.esphome_ns.namespace("GDEP073E01")
GDEP073E01 = gdep073e01_ns.class_(
    "GDEP073E01", display.DisplayBuffer, spi.SPIDevice
)

CONF_BUSY_PIN = "busy_pin"
CONF_RESET_PIN = "reset_pin"
CONF_DC_PIN = "dc_pin"

CONFIG_SCHEMA = display.FULL_DISPLAY_SCHEMA.extend(
    {
        cv.GenerateID(): cv.declare_id(GDEP073E01),
        cv.Required(CONF_BUSY_PIN): cv.use_id(esphome.GPIOPin),
        cv.Required(CONF_RESET_PIN): cv.use_id(esphome.GPIOPin),
        cv.Required(CONF_DC_PIN): cv.use_id(esphome.GPIOPin),
    }
).extend(spi.spi_device_schema(cs_pin_required=True))

async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await display.register_display(var, config)
    await spi.register_spi_device(var, config)

    # Setup pins
    busy_pin = await cg.gpio_pin_expression(config[CONF_BUSY_PIN])
    cg.add(var.set_busy_pin(busy_pin))
    reset_pin = await cg.gpio_pin_expression(config[CONF_RESET_PIN])
    cg.add(var.set_reset_pin(reset_pin))
    dc_pin = await cg.gpio_pin_expression(config[CONF_DC_PIN])
    cg.add(var.set_dc_pin(dc_pin))