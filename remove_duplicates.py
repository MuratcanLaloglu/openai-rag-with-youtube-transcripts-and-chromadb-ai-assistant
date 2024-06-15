def remove_duplicate_links(input_file, output_file):
    unique_links = set()

    with open(input_file, 'r') as f:
        for line in f:
            line = line.strip()
            if line not in unique_links:
                unique_links.add(line)

    with open(output_file, 'w') as f:
        for link in unique_links:
            f.write(link + '\n')

input_file = "video_link.txt"  
output_file = "video_link.txt"  

remove_duplicate_links(input_file, output_file)