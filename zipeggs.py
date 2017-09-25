import logging, os, zc.buildout, sys, shutil

class ZipEggs:
    def __init__(self, buildout, name, options):
        self.name, self.options = name, options
        if options['target'] is None:
            raise zc.buildout.UserError('Invalid Target')
        if options['source'] is None:
            raise zc.buildout.UserError('Invalid Source')


    def zipit(self):
        target_dir = self.options['target']
        if not os.path.exists(target_dir):
            os.makedirs(target_dir)
        source_dir = self.options['source']
        for entry in os.listdir(source_dir):
            try:
                source = os.path.join(source_dir, entry)
                target = "%s/%s" % (target_dir, entry)
                print "%s > %s" % (source, target)
                shutil.make_archive(target, "zip", source)
                os.rename(target+".zip", target)
            except OSError:
                print "ignore %s" % entry
        return []

    def install(self):
        return self.zipit()

    def update(self):
        return self.zipit()
