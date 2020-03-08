class MyConfiguration():

    #setting the configuration of vm instance
    def setconfig():
	
        config = {
            "machineType": "zones/us-central1-a/machineTypes/n1-standard-1",
            "disks":
            [
                {
                    "boot": "True",
                    "initializeParams": {"sourceImage": "projects/debian-cloud/global/images/family/debian-9"}
                }
            ],
            "networkInterfaces": [{"network": "global/networks/default"}]
        }
        return config, self.no_of_vm, self.project_name, self.zone_name
    
    def __init__(self,project_name,zone_name,no_of_vm):
	self.project_name=project_name
	self.zone_name=zone_name
	self.no_of_vm=no_of_vm
	
def main():
	project_name="qwiklabs-gcp-00-832737805b5c"
        zone_name="us-central1-a"
        no_of_vm="2"
	conf= MyConfiguration(project_name,zone_name,no_of_vm)
	conf.setconfig()
		
