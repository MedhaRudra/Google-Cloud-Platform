import googleapiclient.discovery
import json

class MultipleVMInstances:
    
    def new_vm_instance(self):
	
		#reading the config file
        with open('myconfig.json') as f:
            config = json.load(f)
			
		#appending the config file with the name of VM instance
        name= {"name": self.instance_name}
        config.update(name)
        
        resource.instances().insert(project=self.project_name, zone=self.zone_name, body=config).execute()

    def __init__(self, resource, project_name,zone_name,instance_name):
        self.project_name = project_name
        self.zone_name = zone_name
        self.resource = resource
        self.instance_name = instance_name
        
def main(resource):
	#reading the input file
    with open('input_file.json') as i:
        input = json.load(i)
    no_of_vm = int(input['no_of_vm'])
	
    for j in range(0,no_of_vm):
        instance_name= input['instance_name'+'_'+str(j+1)]
		#creating the VM instance
        obj= MultipleVMInstances(resource,"qwiklabs-gcp-01-75b4d3745c78","us-central1-a",instance_name)
        obj.new_vm_instance()

if __name__ == '__main__':
    resource = googleapiclient.discovery.build('compute', 'v1')
    main(resource)
