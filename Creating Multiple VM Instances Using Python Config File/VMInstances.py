import googleapiclient.discovery
from config_file import MyConfiguration

class VMInstances:

    def new_vm_instance(self):

        #reading the config file
        myconfig = self.config()

        #updating the config file with name of vm instance
        name = {"name": self.instance_name}
        myconfig.update(name)

        resource.instances().insert(project=self.project_name, zone=self.zone_name, body = myconfig).execute()

    def __init__(self, resource, project_name, zone_name, instance_name, config):
        self.project_name = project_name
        self.zone_name = zone_name
        self.resource = resource
        self.instance_name = instance_name
        self.config= config

def main(resource):
    #reading the input
    in_arr = []
    in_arr = MyConfiguration.myinput()
    config = in_arr[0]
    no_of_vm = int(in_arr[1])
    project_name = in_arr[2]
    zone_name = in_arr[3]

    vm_name = "my-vm-"

    for j in range(0, no_of_vm):
        instance_name = vm_name+str(j+1)
        #creating new vm instance
        obj = VMInstances(resource, project_name, zone_name, instance_name, config)
        obj.new_vm_instance()

if __name__ == '__main__':
    resource = googleapiclient.discovery.build('compute', 'v1')
    main(resource)
