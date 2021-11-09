import typing

from PySide2.QtWidgets import QFrame, QWidget


class Card(QFrame):
    def __init__(self, parent:typing.Optional[QWidget]=None) -> None:
        """
        Simple QFrame card too fill out the qt custom list

        Args:
            parent: QWidget instance to parent
        """
        super(Card, self).__init__(parent=parent)

        self.setFixedSize(150, 300)
        self.setStyleSheet("background-color: gray;")
        self.setFrameShape(QFrame.StyledPanel)
        self.setFrameShadow(QFrame.Raised)
        self.setLineWidth(3)
        self.setMidLineWidth(3)