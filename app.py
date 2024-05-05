from flask import Flask, jsonify, request

app = Flask(__name__)

# Örnek veri
items = []

# Tüm öğeleri listele
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)

# Yeni bir öğe oluştur
@app.route('/items', methods=['POST'])
def create_item():
    new_item = request.json
    items.append(new_item)
    return jsonify(new_item), 201

# Belirli bir öğeyi al
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    for item in items:
        if item['id'] == item_id:
            return jsonify(item)
    return jsonify({'error': 'Item not found'}), 404

# Belirli bir öğeyi güncelle
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    for item in items:
        if item['id'] == item_id:
            item.update(request.json)
            return jsonify(item)
    return jsonify({'error': 'Item not found'}), 404

# Belirli bir öğeyi sil
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    for index, item in enumerate(items):
        if item['id'] == item_id:
            del items[index]
            return '', 204
    return jsonify({'error': 'Item not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
