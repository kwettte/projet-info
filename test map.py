'''from PyQt5.QtWidgets import QApplication, QGraphicsView, QGraphicsScene
from PyQt5.QtGui import QPixmap

# Création d'une instance d'application PyQT5
app = QApplication([])

# Création d'un objet QGraphicsView
view = QGraphicsView()

# Création d'un objet QGraphicsScene
scene = QGraphicsScene()

# Ajout d'une image de plan à la scène
plan = QPixmap("C:/Users/lucie/Documents/0. ECOLE/ENSTA BRETAGNE/ANNEE 1/SEMESTRE 2/UE 2.1/INFO/TD 4/Ressources/arrierPlan.png")
scene.addPixmap(plan)

# Assignation de la scène à la vue
view.setScene(scene)

# Affichage de la vue
view.show()

# Exécution de l'application PyQT5
app.exec_()'''

from PIL import Image
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.pyplot as plt

img = Image.open(r'PLAN_ENSTA.jpg')
fig, ax = plt.subplots(subplot_kw={'projection': ccrs.PlateCarree()})
ax.imshow(img, origin='upper', transform=ccrs.PlateCarree())
ax.add_feature(cfeature.BORDERS, linewidth=0.5, edgecolor='black')
ax.gridlines(draw_labels=True, linewidth=0.5, color='gray', alpha=0.5, linestyle='--')
plt.show()

'''

import sys
from PyQt5.QtWidgets import QApplication, QGraphicsScene, QGraphicsView, QGraphicsRectItem, QGraphicsLineItem, QGraphicsTextItem
from PyQt5.QtGui import QFont, QColor, QBrush
from PyQt5.QtCore import Qt


class BuildingView(QGraphicsView):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Créer une scène pour dessiner
        self.scene = QGraphicsScene(self)
        self.setScene(self.scene)

        # Activer la selection
        self.setDragMode(QGraphicsView.RubberBandDrag)

        # Dessiner les murs extérieurs du bâtiment
        self.scene.addRect(50, 50, 300, 200)

        # Dessiner les pièces
        self.room1 = self.scene.addRect(60, 60, 100, 80)
        self.room2 = self.scene.addRect(180, 60, 100, 80)
        self.room3 = self.scene.addRect(180, 150, 100, 80)


        # Ajouter des étiquettes
        self.scene.addText("Chambre").setPos(85, 105)
        self.scene.addText("Cuisine").setPos(205, 105)
        self.scene.addText("Salon").setPos(205, 195)

        # Ajouter un signal à l'événement de clic de souris pour les éléments de la scène
        self.scene.selectionChanged.connect(self.onSelectionChanged)

    def onSelectionChanged(self):
        for item in self.scene.selectedItems():
            # Si l'élément sélectionné est une pièce, la colorer en rouge
            if isinstance(item, QGraphicsRectItem) and item != self.room1 and item != self.room2 and item != self.room3:
                item.setBrush(QBrush(Qt.red))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    view = BuildingView()
    view.show()
    sys.exit(app.exec_())

'''