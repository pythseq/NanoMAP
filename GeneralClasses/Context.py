

import sys


 
class ProgramContext:
    def __init__(self, opts):
        self.database_path = None
        self.fastq_path = None 
        self.project_path = 'project'
        self.project_name = ''

        self.threads = '6'
        self.max_memory = '128'
        self.create_database = False
        self.update_taxonomy = False
        self.dump_index = True
        self.read_technology = 'map-ont'
        self.include_plasmids_mitochondria = False

        self.update_params(opts)
        self.check_params_ok()
        self.print_params()


    def update_params(self, opts):
        for opt, arg in opts:
            if opt == '-h':
                self.print_help()
                sys.exit()
            elif opt == '-t':
                self.threads = arg
            elif opt == '-r':
                self.fastq_path = arg
            elif opt == '-d':
                self.database_path = arg
                if not self.database_path.endswith('/'):
                    self.database_path = self.database_path + '/'
            elif opt == '-p':
                self.project_name = arg
                self.project_path = 'projects/' + arg
            elif opt == '-m':
                self.max_memory = int(arg) // 4 * 3
            elif opt == '--map-pb':
                self.read_technology = 'map-pb'
            elif opt == '--allow-extrachromosomal':
                self.include_plasmids_mitochondria = True
                

    def print_help(self):
        print('\nno help for now\n')
    

    def check_params_ok(self):
        if self.fastq_path is None or self.database_path is None:
            print('\nincomplete args\n')
            self.print_help()


    def print_params(self):
        print('\nNanoMAP parameters:')
        for key, val in vars(self).items():
            print(key, ":", val)


class StrainGroupingContext:
    # [context.project_path, context.database_path, context.fastq_path]
    def __init__(self, args):
        self.project_path = args[0]
        self.database_path = args[1]
        self.fastq_path = args[2]
        self.paf = args[0] + '/runtimefiles/pafs/full_alignment.paf'


    
class GroupContext:
    def __init__(self, args):
        self.group_id = args[0]
        self.group_abundance = args[1]
        self.project_path = args[2]
        self.read_technology = args[3]
        self.threads = args[4]



class DatabaseBuildingContext:
    def __init__(self, opts):
        self.database_path = None
        self.taxonomy_path = None
        self.read_technology_preset = 'map-ont'
        self.threads = '3'
        self.rebuild = False
        self.max_memory = '128'
        self.update_params(opts)


    def update_params(self, opts):
        for opt, arg in opts:
            if opt == '-h':
                self.print_help()
                sys.exit()
            elif opt == '-d':
                self.database_path = arg
                if not self.database_path.endswith('/'):
                    self.database_path = self.database_path + '/'
            elif opt == '-p':
                self.read_technology_preset = arg
            elif opt == '-m':
                self.max_memory = int(arg) // 4 * 3
            elif opt == '--rebuild':
                self.rebuild = True
            

    def print_help(self):
        print('HELP MESSAGE')
        print('This program builds a NanoMAP database.')
        print('A database must be build before characterising read sets.')
        print('{:50}{:10}{:50}'.format('Argument description', 'flag', '[valid inputs]\n'))
        print('Required arguments:')
        print('{:50}{:10}{:50}'.format('A folder containing genome FASTAs:', '-d', '[folder path (can be relative)]\n'))
        print('Optional arguments:')
        print('{:50}{:10}{:50}'.format('Read technology preset:', '-p', '[either map-ont (ONT) or map-pb (PacBio)]'))
        print('{:50}{:10}{:50}'.format('Max RAM usage (Gigabytes):', '-m', '[num gigabytes]\n'))
        





class ResContext:
    def __init__(self, argv):
        self.database_path = argv[0]
        self.project_path = argv[1]
        self.group_name = argv[2]
        self.group_databases_path = self.project_path + '/group_databases/'
        self.reference_genome_filename_dump = self.group_databases_path + '/group_reference_genomes/' + self.group_name + '_reference_genomes.txt'
        self.fastq_file = self.project_path + '/group_fastqs/' + self.group_name + '.fq'
        self.threads = '4'