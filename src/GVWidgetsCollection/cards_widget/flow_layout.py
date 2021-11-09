import math

from typing import List, Optional
from PySide2.QtCore import Signal, Qt
from PySide2.QtWidgets import QGridLayout, QWidget
from PySide2.QtGui import QResizeEvent

from GVWidgetsCollection.cards_widget.card import Card


class FlowLayout(QGridLayout):
    """
    This widget provide a way to handle many widgets and auto positionate them following the window size

    Attributes:
        on_window_resize: This qt signal is emmited every time the widget is resized.
        cards_position_update: This qt signal is emmited every time the Cards position is updated.

    """
    on_window_resize : Signal = Signal(QResizeEvent)
    cards_position_updated : Signal = Signal()

    def __init__(self, cards:Optional[List[Card]]=None, parent:Optional[QWidget]=None) -> None:
        """
        Layout to handle widgets like cards. Able to resize and realocate the widgets positions.

        Args:
            cards: List of ``Card`` instance.
            parent: The parent instance of this widget.
        """
        super(FlowLayout, self).__init__(parent)
        self.on_window_resize.connect(self._update_pos_matrix)

        self._cards = cards or []
        self._matrix = None
        self.offset = 0
        self.cards_alignment = Qt.AlignTop | Qt.AlignLeft
    
    @property
    def cards(self) -> List[Card]:
        """
        Get cards

        Returns:
            The current card list.
        """
        return self._cards

    @cards.setter
    def cards(self, cards: List[Card]) -> None:
        """
        Set cards

        Args:
            cards: A new card list instance.
        """
        self.remove_all()
        self._cards = cards
        self._update_pos_matrix()
    
    def add_card(self, card: Card) -> None:
        """
        Add new card instance on the current card list.

        Args:
            card: The ``Card`` instance to add.
        """
        self._cards.append(card)
        self._update_pos_matrix()

    def remove_all(self) -> None:
        """Remove all widgets from the layout"""
        for c in self._cards:
            self.removeWidget(c)
            c.deleteLater()
        self._cards = []

    def _update_pos_matrix(self, event: Optional[QResizeEvent]=None) -> None:
        """
        Set the widget positions based on the current window size.

        Args:
            event: The window resize Event. 
                   If None, this method will try to get the window size following the parent widget.
        """
        size = event.size() if event else self.parent().size()
        current_width = size.width()
        item_len = len(self._cards)
        width = self._cards[0].size().width() if item_len else 1
        max_item_width = math.ceil(width + ((width * self.offset) / 100.0))
        
        max_col = int(current_width / max_item_width) or 1
        max_row = int(item_len / max_col) + (item_len % max_col > 0)

        self._matrix = [(i, j) for j in range(max_col) for i in range(max_row)]
        self._matrix.sort()
        
        self._update_cards_position()

    def _update_cards_position(self) -> None:
        """Update the cards position following the last window resize event."""
        for index, card in enumerate(self._cards):
            self.removeWidget(card)
            self.addWidget(card, *self._matrix[index], self.cards_alignment)
        
        self.cards_position_updated.emit()