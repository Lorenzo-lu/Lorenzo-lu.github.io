import sys,os, shutil

def main():
	origin_root = '/virtual_root/';
	new_root = 'https://foobar.yizhoulu.repl.co/virtual_root/';
	new_root = '/virtual_root/'
	
	cur_path = os.getcwd();
	#Console
	web_file_path = os.path.join(os.getcwd(), 'virtual_root_template/');
	#web_file_path = 'C:/Users/ylu289/Downloads/homepage';
	copy_web_file_path = os.path.join(os.getcwd(), 'virtual_root/');
	if os.path.exists(copy_web_file_path):
		shutil.rmtree(copy_web_file_path);
	# shutil.copytree(web_file_path, copy_web_file_path) 
	os.mkdir(copy_web_file_path);
	# print(os.listdir(copy_web_file_path))
	
	
	def transform(web_file_path, copy_web_file_path, origin_root, new_root):
		cur_path = os.getcwd();	
		print(cur_path)
		os.chdir(web_file_path);
		file_list = os.listdir();
		for file in file_list:
			if os.path.isdir(file):
				# print(os.path.join(web_file_path, '%s'%(file)))
				os.mkdir(os.path.join(copy_web_file_path, '%s'%(file)))
				transform(os.path.join(web_file_path, '%s'%(file)), os.path.join(copy_web_file_path, '%s'%(file)), origin_root, new_root);
			else:
				try:
					f = open(file,'r', encoding="utf8");
					content = f.read();
					f.close();
					transformed = ('%s'%new_root).join(content.split('%s'%origin_root));
					# os.remove(file);
					f = open(os.path.join(copy_web_file_path, '%s'%(file)), 'a',encoding="utf8");
					f.write(transformed);
					f.close();     
					print('File processed: %s'%(os.getcwd()+'/'+file))			
				except Exception as e:	
					# os.remove(file);
					shutil.copyfile(os.path.join(web_file_path, '%s'%(file)), os.path.join(copy_web_file_path, '%s'%(file)))
					print('Encounter a unreadable file: %s'%(os.getcwd()+'/'+file));
					print(e);
		os.chdir(cur_path);
	
	# os.chdir(copy_web_file_path)
	try:
		transform(web_file_path, copy_web_file_path, origin_root, new_root);
	except Exception as e:
		print('Error!'); print(e);
		os.chdir(cur_path);

if __name__ == '__main__':
	main();