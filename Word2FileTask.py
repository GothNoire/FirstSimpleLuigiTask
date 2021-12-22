import luigi

class WordFileTask (luigi.Task):
    word = luigi.Parameter()
    filename = luigi.Parameter()

    def run (self):
        with self.output().open('w') as f:
            f.write(self.word)

    def output(self):
        return luigi.LocalTarget(self.filename)

class MainFileTask (luigi.Task):

    mainFileName = luigi.Parameter()
    firstWord = luigi.Parameter()
    secondWord = luigi.Parameter()

    def requires(self):
        return [
            WordFileTask(word = self.firstWord, filename = 'FirstFiletmp.txt'),
            WordFileTask(word= self.secondWord, filename = 'SecondFiletmp.txt')
        ]

    def output(self):
        return luigi.LocalTarget(self.mainFileName)

    def run(self):
        "get all Target from requires"
        first, second = self.input()
        with self.output().open('w') as m:
            with first.open() as f, second.open() as s:
                m.write('{} {}'.format(f.read(), s.read()))