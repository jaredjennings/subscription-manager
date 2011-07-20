import unittest
import datetime

import stubs
from subscription_manager.gui import contract_selection
from subscription_manager import managerlib


def stubSelectedCallback(self, pool):
    pass


def stubCancelCallback(self):
    pass


class ContractSelection(unittest.TestCase):
    pool = {'productName': 'SomeProduct',
            'consumed': "consumed",
            'quantity': 'quantity',
            'startDate': datetime.datetime.now(tz=managerlib.ServerTz(0)).isoformat(),
            'endDate': datetime.datetime.now(tz=managerlib.ServerTz(0)).isoformat(),
            'contractNumber': 'contractNumber'}

    def test_contract_selection_show(self):
        cs = contract_selection.ContractSelectionWindow(selected_callback=stubSelectedCallback,
                                                        cancel_callback=stubCancelCallback)
        cs.show()

    def test_contract_selection_add_pool(self):
        cs = contract_selection.ContractSelectionWindow(selected_callback=stubSelectedCallback,
                                                         cancel_callback=stubCancelCallback)
        cs.add_pool(self.pool, 4)
