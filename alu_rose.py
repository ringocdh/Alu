# alu_rose.py

import time
import os

rose_art = r"""
       .     .
    ...  :``..':
     : ````.'   :''::'
   ..:..  :     .'' :
``.    `:    .'     :
    :    :   :        :
     :   :   :         :
     :    :   :        :
      :    :   :..''''``::.
       : ...:..'     .''
       .'   .'  .::::'
      :..'''``:::::::
      '         `::::
                  `::.
                   `::
                    :::.
         ..:.:.::'`. ::'`.  . : : .
       ..'      `:.: ::   :'       .:
      .:        .:``:::  :       .: ::
      .:    ..''     :::.'    :':    :
       : .''         .:: : : '
        :          .'`::
                      ::
                      ::
                      ::
                      ::
"""

message = "\nWürdest du mit mir auf ein Date gehen, Alu?? ❤️"

os.system('cls' if os.name == 'nt' else 'clear')
print(rose_art)
time.sleep(1)
print(message)
