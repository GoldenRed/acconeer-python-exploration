from collections import namedtuple

from acconeer_utils.clients import configs

from helper import UnsqueezingDummyProcessor

import service_modules.envelope as envelope_module
import service_modules.iq as iq_module
import service_modules.sparse as sparse_module
import examples.services.power_bin as power_bin_module
import examples.processing.breathing as breathing_module
import examples.processing.phase_tracking as phase_tracking_module
import examples.processing.presence_detection_iq as presence_detection_iq_module
import examples.processing.presence_detection_sparse as presence_detection_sparse_module
import examples.processing.sleep_breathing as sleep_breathing_module
import examples.processing.obstacle_detection as obstacle_detection_module


ModuleInfo = namedtuple("ModuleInfo", [
    "label",
    "module",
    "sensor_config_class",
    "processor",
    "processing_config_class",
])

MODULE_INFOS = [
    ModuleInfo(
        "Select service",
        None,
        None,
        None,
        None,
    ),
    ModuleInfo(
        "IQ",
        iq_module,
        configs.IQServiceConfig,
        iq_module.IQProcessor,
        iq_module.get_processing_config,
    ),
    ModuleInfo(
        "Envelope",
        envelope_module,
        configs.EnvelopeServiceConfig,
        envelope_module.EnvelopeProcessor,
        envelope_module.get_processing_config,
    ),
    ModuleInfo(
        "Power bin",
        power_bin_module,
        configs.PowerBinServiceConfig,
        UnsqueezingDummyProcessor,
        None,
    ),
    ModuleInfo(
        "Sparse",
        sparse_module,
        sparse_module.get_sensor_config,
        sparse_module.Processor,
        sparse_module.get_processing_config,
    ),
    ModuleInfo(
        "Breathing",
        breathing_module,
        breathing_module.get_sensor_config,
        breathing_module.BreathingProcessor,
        breathing_module.get_processing_config,
    ),
    ModuleInfo(
        "Phase tracking",
        phase_tracking_module,
        phase_tracking_module.get_sensor_config,
        phase_tracking_module.PhaseTrackingProcessor,
        phase_tracking_module.get_processing_config,
    ),
    ModuleInfo(
        "Presence detection (IQ)",
        presence_detection_iq_module,
        presence_detection_iq_module.get_sensor_config,
        presence_detection_iq_module.PresenceDetectionProcessor,
        presence_detection_iq_module.get_processing_config,
    ),
    ModuleInfo(
        "Presence detection (sparse)",
        presence_detection_sparse_module,
        presence_detection_sparse_module.get_sensor_config,
        presence_detection_sparse_module.PresenceDetectionSparseProcessor,
        presence_detection_sparse_module.get_processing_config,
    ),
    ModuleInfo(
        "Sleep breathing",
        sleep_breathing_module,
        sleep_breathing_module.get_sensor_config,
        sleep_breathing_module.PresenceDetectionProcessor,
        sleep_breathing_module.get_processing_config,
    ),
    ModuleInfo(
        "Obstacle detection",
        obstacle_detection_module,
        obstacle_detection_module.get_sensor_config,
        obstacle_detection_module.ObstacleDetectionProcessor,
        obstacle_detection_module.get_processing_config,
    ),
]

MODULE_LABEL_TO_MODULE_INFO_MAP = {mi.label: mi for mi in MODULE_INFOS}
