# -*- coding: utf-8 -*-

class GildedRose(object):
    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            self.update_item_quality(item)

    def update_item_quality(self, item):
        if item.name == "Aged Brie":
            self.update_aged_brie(item)
        elif item.name == "Backstage passes to a TAFKAL80ETC concert":
            self.update_backstage_passes(item)
        elif item.name == "Sulfuras, Hand of Ragnaros":
            pass  # Sulfuras não precisa ser atualizado
        elif item.name.startswith("Conjured"):
            self.update_conjured_item(item)
        else:
            self.update_regular_item(item)
        
        if item.name != "Sulfuras, Hand of Ragnaros":
            item.sell_in -= 1
        
        if item.sell_in < 0:
            self.handle_expired_item(item)

    def update_aged_brie(self, item):
        if item.quality < 50:
            item.quality += 1

    def update_backstage_passes(self, item):
        if item.quality < 50:
            item.quality += 1
            if item.sell_in < 11 and item.quality < 50:
                item.quality += 1
            if item.sell_in < 6 and item.quality < 50:
                item.quality += 1

    def update_regular_item(self, item):
        if item.quality > 0:
            item.quality -= 1

    def update_conjured_item(self, item):
        if item.quality > 0:
            item.quality -= 2

    def handle_expired_item(self, item):
        if item.name == "Aged Brie":
            if item.quality < 50:
                item.quality += 1
        elif item.name == "Backstage passes to a TAFKAL80ETC concert":
            item.quality = 0
        elif item.name.startswith("Conjured"):
            if item.quality > 0:
                item.quality -= 2
        elif item.name != "Sulfuras, Hand of Ragnaros":
            if item.quality > 0:
                item.quality -= 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
