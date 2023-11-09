import xml.etree.ElementTree as ET

def create_annotation(path, objects):
    root = ET.Element('annotation')
    path_components = path.split('/')
    folder_text = path_components[-2]
    filename_text = path_components[-1]
    width_value = 416
    height_value = 416
    channels_value = 3

    folder = ET.SubElement(root, 'folder')
    folder.text = folder_text

    filename = ET.SubElement(root, 'filename')
    filename.text = filename_text

    size = ET.SubElement(root, 'size')
    width = ET.SubElement(size, 'width')
    width.text = str(width_value)
    height = ET.SubElement(size, 'height')
    height.text = str(height_value)
    channel = ET.SubElement(size, 'channel')
    channel.text = str(channels_value)

    for obj in objects:
        object = ET.SubElement(root, 'object')
        name = ET.SubElement(object, 'name')
        name.text = obj['name']

        difficult = ET.SubElement(object, 'difficult')
        difficult.text = str(obj['check_box'][0])
        truncate = ET.SubElement(object, 'truncated')
        truncate.text = str(obj['check_box'][1])
        occluded = ET.SubElement(object, 'occluded')
        occluded.text = str(obj['check_box'][2])

        bnd_box = ET.SubElement(object, 'bndbox')
        xmin = ET.SubElement(bnd_box, 'xmin')
        xmin.text = str(min(obj['bnd_dim'][0], obj['bnd_dim'][2]))
        ymin = ET.SubElement(bnd_box, 'ymin')
        ymin.text = str(min(obj['bnd_dim'][1], obj['bnd_dim'][3]))
        xmax = ET.SubElement(bnd_box, 'xmax')
        xmax.text = str(max(obj['bnd_dim'][0], obj['bnd_dim'][2]))
        ymax = ET.SubElement(bnd_box, 'ymax')
        ymax.text = str(max(obj['bnd_dim'][1], obj['bnd_dim'][3]))

    tree = ET.ElementTree(root)
    new_path = "/".join(path_components[:-1])
    new_path += "/" + filename_text.split(".")[0] + ".xml"
    tree.write(new_path)


#create_annotation('/Users/klsharma22/Desktop/NextGenTechInc/Object Detection/Model/Custom-made/data/gerenuk/image_0034.jpg',[{'name': 'gerunk', 'bnd_dim': [0, 0, 0, 0], 'check_box': [0, 0, 0]}, {'name': 'gerunk', 'bnd_dim': [0, 0, 0, 0], 'check_box': [0, 0, 0]}])
