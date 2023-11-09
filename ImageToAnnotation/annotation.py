import xml.etree.ElementTree as ET

def create_annotation(path, bnd_dim, check_box_values):
    root = ET.Element('annotation')
    path_components = path.split('/')
    folder_text = path_components[-2]
    filename_text = path_components[-1]
    width_value = 416
    height_value = 416
    channels_value = 3
    object_name_text = folder_text
    xmin_value = min(bnd_dim[0], bnd_dim[2])
    ymin_value = min(bnd_dim[1], bnd_dim[3])
    xmax_value = max(bnd_dim[0], bnd_dim[2])
    ymax_value = max(bnd_dim[1], bnd_dim[3])

    difficult_value = check_box_values[0]
    truncated_value = check_box_values[1]
    occluded_value = check_box_values[2]

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

    object = ET.SubElement(root, 'object')
    name = ET.SubElement(object, 'name')
    name.text = object_name_text

    difficult = ET.SubElement(object, 'difficult')
    difficult.text = str(difficult_value)
    truncate = ET.SubElement(object, 'truncated')
    truncate.text = str(truncated_value)
    occluded = ET.SubElement(object, 'occluded')
    occluded.text = str(occluded_value)

    bnd_box = ET.SubElement(object, 'bndbox')
    xmin = ET.SubElement(bnd_box, 'xmin')
    xmin.text = str(xmin_value)
    ymin = ET.SubElement(bnd_box, 'ymin')
    ymin.text = str(ymin_value)
    xmax = ET.SubElement(bnd_box, 'xmax')
    xmax.text = str(xmax_value)
    ymax = ET.SubElement(bnd_box, 'ymax')
    ymax.text = str(ymax_value)

    tree = ET.ElementTree(root)
    tree.write(filename_text.split('.')[0] + '.xml')

