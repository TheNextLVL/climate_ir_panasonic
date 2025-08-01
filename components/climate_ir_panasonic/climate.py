import esphome.codegen as cg
from esphome.components import climate_ir

AUTO_LOAD = ["climate_ir"]

climate_ir_panasonic_ns = cg.esphome_ns.namespace("climate_ir_panasonic")
PanasonicClimate = climate_ir_panasonic_ns.class_("PanasonicClimate", climate_ir.ClimateIR)

CONFIG_SCHEMA = climate_ir.climate_ir_with_receiver_schema(PanasonicClimate)

async def to_code(config):
    await climate_ir.new_climate_ir(config)
