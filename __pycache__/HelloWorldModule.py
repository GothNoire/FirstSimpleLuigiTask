import luigi

class HelloTask (luigi.Task):
    word = 'Hello'
    filename = 'Hello.txt'
    "Write hello to hello.txt"
    #word ##= luigi.parameter()
    #filename ##= luigi.parameter()

    # def __init__(self):
    #     self.word = 'Hello'
    #     self.filename = 'Hello.txt'

    def run (self):
        with self.output().open('w') as f:
            f.write(self.word)

    def output(self):
        return luigi.LocalTarget(self.filename)

class WorldTask (luigi.Task):
    "Write world to world.txt"
    word = 'World'
    filename = 'World.txt'
    # word = luigi.parameter()
    # filename = luigi.parameter()

    # def __init__(self):
    #     self.word = 'Hello'
    #     self.filename = 'World.txt'

    def run (self):
        with self.output().open('w') as f:
            f.write(self.word)
    def output (self):
        return luigi.LocalTarget(self.filename)

class HelloWorldTask (luigi.Task):
    "Concat two earlies task and write result into new file"
    #filename = luigi.parameter()
    filename = 'HelloWorld.txt'
    # def __init__(self):
    #     self.filename = 'HelloWorld.txt'

    def requires(self):
        return [
            HelloTask(),
            WorldTask()
        ]

    def run(self):
        "get all Target from requires"
        hello, world = self.input()
        with self.output().open('w') as out:
            with hello.open() as h, world.open() as w:
                out.write('{} {}\n'.format(h.read(), w.read()))

    def output(self):
        return luigi.LocalTarget(self.filename)