import sys
import pandas as pd
from PyQt5.QtWidgets import QApplication, QTableView
from PyQt5.QtCore import QAbstractTableModel, Qt

# Tạo lớp để tạo model từ DataFrame
class PandasModel(QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self._data = data

    def rowCount(self, index):
        return self._data.shape[0]

    def columnCount(self, index):
        return self._data.shape[1]

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid() and role == Qt.DisplayRole:
            return str(self._data.iloc[index.row(), index.column()])
        return None

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return self._data.columns[section]
            if orientation == Qt.Vertical:
                return str(self._data.index[section])
        return None

# Tạo DataFrame
data = {
    'Tên': ['Alice', 'Bob', 'Charlie', 'David'],
    'Tuổi': [24, 27, 22, 32],
    'Điểm': [85, 90, 78, 88]
}
df = pd.DataFrame(data)

# Tạo ứng dụng PyQt
app = QApplication(sys.argv)
model = PandasModel(df)
view = QTableView()
view.setModel(model)
view.setWindowTitle("DataGridView with PyQt5")
view.show()
sys.exit(app.exec_())
