import matplotlib.pyplot as plt

# Dados de mAP50-95 para cada modelo
batch_sizes = [2, 4, 8, 16]
yolov5_map5095 = [49.821, 55.908, 60.488, 56.739]
yolov6_map5095 = [50.705, 54.108, 53.128, 56.739]
yolov7_map5095 = [53.45, 56.807, 54.71, 52.53]
yolov8_map5095 = [61.710, 65.201, 66.451, 68.245]

# Criando o gráfico
plt.figure(figsize=(8,6))
plt.plot(batch_sizes, yolov5_map5095, marker='o', label='YOLOv5', color='yellow', linewidth=2)
plt.plot(batch_sizes, yolov6_map5095, marker='s', label='YOLOv6', color='green', linewidth=2)
plt.plot(batch_sizes, yolov7_map5095, marker='^', label='YOLOv7', color='red', linewidth=2)
plt.plot(batch_sizes, yolov8_map5095, marker='^', label='YOLOv8', color='blue', linewidth=2)

# Adicionando rótulos e título
plt.xlabel('Batch Size', fontsize=12)
plt.ylabel('mAP50-95 (%)', fontsize=12)
plt.title('Comparação de mAP50-95 em diferentes tamanhos de Batch', fontsize=14)

# Exibindo a legenda
plt.legend()

# Exibindo a grade
plt.grid(True)

# Mostrando o gráfico
plt.show()
