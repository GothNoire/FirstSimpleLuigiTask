# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import luigi
from luigi import parameter

class HelloTask (luigi.Task):
    word = 'Hello'
    filename = 'Hello.txt'

    "Write hello to hello.txt"
    def run (self):
        with self.output().open('w') as f:
            f.write(self.word)

    def output(self):
        return luigi.LocalTarget(self.filename)

class WorldTask (luigi.Task):
    "Write world to world.txt"
    word = 'World'
    filename = 'World.txt'

    def run (self):
        with self.output().open('w') as f:
            f.write(self.word)
    def output (self):
        return luigi.LocalTarget(self.filename)

class HelloWorldTask (luigi.Task):
    "Concat two earlies task and write result into new file"
    filename = 'HelloWorld.txt'

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


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    luigi.build([HelloWorldTask()], local_scheduler=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
