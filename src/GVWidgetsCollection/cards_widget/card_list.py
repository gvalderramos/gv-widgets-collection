import typing

from PySide2.QtCore import Signal, Qt
from PySide2.QtWidgets import QScrollArea, QWidget
from PySide2.QtGui import QResizeEvent

from GVWidgetsCollection.cards_widget.card import Card
from GVWidgetsCollection.cards_widget.flow_layout import FlowLayout


class CardList(QScrollArea):
    class CardContainer(QWidget):
        _window_resized = Signal(QResizeEvent)

        def __init__(self, parent: typing.Optional[QWidget]=None) -> None:
            """
            Widget to handle all cards instance

            Args:
                parent: The parent widget instance
            """
            super(CardList.CardContainer, self).__init__(parent)
            self.flow_layout = FlowLayout()
            self._window_resized.connect(self.flow_layout.on_window_resize)
            self.setLayout(self.flow_layout)

    def __init__(self, parent: typing.Optional[QWidget]=None) -> None:
        """
        Custom list widget

        Args:
            parent: The parent widget instance
        """
        super(CardList, self).__init__(parent=parent)
        
        self._card_container = self.CardContainer()
        self.setWidget(self._card_container)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setWidgetResizable(True)

    def set_cards(self, cards: typing.List[Card]) -> None:
        """
        Set the card list

        Args:
            cards: The ``Card`` instance list
        """
        self._card_container.flow_layout.cards = cards

    def add_card(self, card: Card) -> None:
        """
        Add one card instance to the list

        Args:
            card: The ``Card`` instance
        """
        self._card_container.flow_layout.add_card(card)
    
    def remove_cards(self) -> None:
        """Remove all cards from the current list"""
        self._card_container.flow_layout.remove_all()
    
    def resizeEvent(self, event: QResizeEvent) -> None:
        """
        This method is called every time the current window is resized

        Args:
            event: The ``QResizeEvent`` instance.
        """
        self._card_container._window_resized.emit(event)
        return super().resizeEvent(event)