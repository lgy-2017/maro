# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license.

from typing import List

from .virtual_machine import VirtualMachine


class Action:
    """Data center scenario action object, which was used to pass action from agent to business engine.

    Args:
        vm (VirtualMachine): The virtual machine object, which only contains id, requirement resource, lifetime.
        pm_id (int): The physical machine id assigned to this vm.
        buffer_time (int): The remaining buffer time to assign this VM.
    """

    def __init__(self, assign: bool, vm_req: VirtualMachine, buffer_time: int, pm_id: int = None):
        self.assign = assign
        self.vm_req = vm_req
        self.pm_id = pm_id
        self.buffer_time = buffer_time


class VmRequirementPayload:
    """Payload for the VM requirement.

    Args:
        vm_info (VirtualMachine): The VM information
        buffer_time (int): The remaining buffer time
    """

    summary_key = ["vm_info", "buffer_time"]

    def __init__(self, vm_req: VirtualMachine, buffer_time: int):
        self.vm_req = vm_req
        self.buffer_time = buffer_time


class VmFinishedPayload:
    """Payload for the VM finished.

    Args:
        vm_id (int): The id of the VM in the end cycle.
    """

    summary_key = ["vm_id"]

    def __init__(self, vm_id: int):
        self.vm_id = vm_id


class DecisionEvent:
    """Decision event in Data center scenario that contains information for agent to choose action.


    """

    def __init__(self, valid_pm: List[int], vm_info: VirtualMachine, buffer_time: int):
        self.valid_pm = valid_pm
        self.vm_info = vm_info
        self.buffer_time = buffer_time


class Latency:
    """Accumulated latency.

    1. Triggered by the resource exhaustion (resource_buffer_time).
    2. Triggered by the algorithm inaccurate predictions (algorithm_buffer_time).
    """
    def __init__(self):
        self.latency_due_to_agent: int = 0
        self.latency_due_to_resource: int = 0
