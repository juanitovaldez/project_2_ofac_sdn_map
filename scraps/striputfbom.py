ff_name = 'eu_sdn_pretty.json'
target_file_name = 'eu_sdn_pretty_bomstrip.json'
with open(ff_name, 'rb') as source_file:
  with open(target_file_name, 'w+b') as dest_file:
    contents = source_file.read()
    dest_file.write(contents.decode('utf-16').encode('utf-8'))