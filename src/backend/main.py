from argparse import ArgumentParser
from migrations.migrations import execute_migrations
from serve import serve_app

def main():
  parser = ArgumentParser()
  parser.add_argument("-p", "--production",
                      dest="production_mode",
                      default=False,
                      action='store_true',
                      help="run program in production mode, else runs in development mode")
  parser.add_argument("-m", "--migrate",
                      dest="migrate",
                      default=False,
                      action='store_true',
                      help="run migration scripts")

  args = parser.parse_args()
  args = vars(args)
  
  if(args['migrate']):
    execute_migrations()
  
  serve_app(production=args['production_mode'])
  
if __name__ == "__main__":
  main()