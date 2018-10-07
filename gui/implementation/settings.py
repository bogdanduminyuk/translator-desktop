from PyQt5.QtGui import QFont

from gui.base.settings import Ui_DialogSettings
from core.settings import user


class Ui_DialogSettingsImplementation(Ui_DialogSettings):
    def setupUi(self, DialogSettings):
        super(Ui_DialogSettingsImplementation, self).setupUi(DialogSettings)
        self.lineEditAppId.setText(user["general"]["application_id"])
        self.lineEditAppKey.setText(user["general"]["application_key"])

        self.spinBoxOutSynCount.setValue(user["output"]["synonyms_count"])
        self.spinBoxOutAntCount.setValue(user["output"]["antonyms_count"])

        self.spinBoxRequestTimeout.setValue(user["advanced"]["request_timeout"])
        self.spinBoxRequestInterval.setValue(user["advanced"]["request_interval"])
        self.spinBoxSaveCategoryCount.setValue(user["advanced"]["database"]["save_category_senses_count"])
        self.spinBoxSaveItemsCount.setValue(user["advanced"]["database"]["save_items_count"])

        self.fontComboBox.setCurrentFont(QFont(user["docx-writer"]["font-family"]))

        idx = self.sizeComboBox.findText(user["docx-writer"]["font-size"])
        self.sizeComboBox.setCurrentIndex(idx)

        idx = self.intervalComboBox.findText(user["docx-writer"]["line-spacing"])
        self.intervalComboBox.setCurrentIndex(idx)

        margin = user["docx-writer"]["margin"]
        self.doubleSpinBoxMarginTop.setValue(margin[0])
        self.doubleSpinBoxMarginRight.setValue(margin[1])
        self.doubleSpinBoxMarginBottom.setValue(margin[2])
        self.doubleSpinBoxMarginLeft.setValue(margin[3])
