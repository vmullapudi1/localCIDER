""" 
   !--------------------------------------------------------------------------!
   ! LICENSE INFO:                                                            !
   !--------------------------------------------------------------------------!
   !    This file is part of localCIDER.                                      !
   !                                                                          !
   !    Version 0.1.6                                                         !
   !                                                                          !
   !    Copyright (C) 2014, The localCIDER development team (current and      !
   !                        former contributors): Alex Holehouse, James       !
   !                        Ahad, Rahul K. Das.                               !
   !                                                                          !
   !    localCIDER was developed in the lab of Rohit Pappu at Washington      !
   !    University in St. Louis. Please see the website for citation          !
   !    information:                                                          !
   !                                                                          !
   !    http://pappulab.github.io/localCIDER/                                 !
   !                                                                          !
   !    For more information please see the Pappu lab website:                !
   !                                                                          !
   !    http://pappulab.wustl.edu/                                            !
   !                                                                          !
   !    localCIDER is free software: you can redistribute it and/or modify    !
   !    it under the terms of the GNU General Public License as published by  !
   !    the Free Software Foundation, either version 3 of the License, or     !
   !    (at your option) any later version.                                   !
   !                                                                          !
   !    localCIDER is distributed in the hope that it will be useful,         !
   !    but WITHOUT ANY WARRANTY; without even the implied warranty of        !
   !    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         !
   !    GNU General Public License for more details.                          !
   !                                                                          !
   !    You should have received a copy of the GNU General Public License     !
   !    along with localCIDER.  If not, see <http://www.gnu.org/licenses/>.   !
   !--------------------------------------------------------------------------!
   ! AUTHORSHIP INFO:                                                         !
   !--------------------------------------------------------------------------!
   !                                                                          !
   ! MAIN AUTHOR:    Alex Holehouse                                           !
   !                                                                          !
   !--------------------------------------------------------------------------!

   Maxmimum complexity values, where complexity is the length of the zlib. zlib 
   uses DEFLATE, which is a combo of Huffman coding and LZ77, which means it facilitates
   lossless compression limited, fundementally, by the entropy of the string. In the interest
   of efficiency we precompute the maximally long (i.e. complex) values for strings
   of length 1 to 1,000. We're currently crunching the numbers to increase this maximum size

   An important point here is that by leveraging Huffman coding we implicitly capture patterning
   as well as composition. Specifically, from a Huffman coding perspective

   GGGLLLGGGLL 

   is a lower complexity than

   GLGLLGGLGLGL

   Despite the sequences having the same amino acid composition.

   Note that this is NOT the same as most low complexity measures. This is currently
   an experimental approach and has not been tested for rigour (and is not included in the
   main localcider documentation or SequenceParameters object calls for this reason).

   Basically - you're welcome to think about complexity in this way, but it may not be a good
   way of doing it!

"""

# the sequences here represent heurstic close approxiations to the most complex sequence which could be created using a string of 20 amino acids of length KEY.
# where we define complexity as compressed = len(zlib.compress(seq)) where seq is the raw amino acid sequence.



maxComplexity = {5 : 13, 6 : 14, 7 : 15, 8 : 16, 9 : 17, 10 : 18, 11 : 19, 12 : 20, 13 : 21, 14 : 22, 15 : 23, 16 : 24, 17 : 25, 18 : 26, 19 : 27, 20 : 28, 21 : 29, 22 : 30, 23 : 31, 24 : 32, 25 : 33, 26 : 34, 27 : 35, 28 : 36, 29 : 37, 30 : 38, 31 : 39, 32 : 40, 33 : 41, 34 : 42, 35 : 43, 36 : 44, 37 : 45, 38 : 46, 39 : 47, 40 : 48, 41 : 49, 42 : 50, 43 : 50, 44 : 51, 45 : 52, 46 : 53, 47 : 54, 48 : 54, 49 : 55, 50 : 56, 51 : 56, 52 : 57, 53 : 57, 54 : 58, 55 : 58, 56 : 60, 57 : 59, 58 : 60, 59 : 61, 60 : 62, 61 : 62, 62 : 63, 63 : 63, 64 : 63, 65 : 64, 66 : 65, 67 : 65, 68 : 66, 69 : 66, 70 : 67, 71 : 68, 72 : 68, 73 : 69, 74 : 69, 75 : 70, 76 : 71, 77 : 71, 78 : 72, 79 : 72, 80 : 73, 81 : 73, 82 : 74, 83 : 74, 84 : 75, 85 : 75, 86 : 76, 87 : 77, 88 : 77, 89 : 78, 90 : 78, 91 : 79, 92 : 80, 93 : 80, 94 : 81, 95 : 81, 96 : 82, 97 : 82, 98 : 83, 99 : 83, 100 : 84, 101 : 85, 102 : 86, 103 : 86, 104 : 87, 105 : 87, 106 : 88, 107 : 88, 108 : 89, 109 : 89, 110 : 90, 111 : 90, 112 : 91, 113 : 92, 114 : 92, 115 : 93, 116 : 93, 117 : 94, 118 : 94, 119 : 95, 120 : 96, 121 : 96, 122 : 97, 123 : 97, 124 : 98, 125 : 98, 126 : 99, 127 : 100, 128 : 100, 129 : 101, 130 : 101, 131 : 102, 132 : 102, 133 : 103, 134 : 103, 135 : 104, 136 : 104, 137 : 105, 138 : 106, 139 : 106, 140 : 107, 141 : 107, 142 : 108, 143 : 108, 144 : 109, 145 : 109, 146 : 110, 147 : 111, 148 : 111, 149 : 111, 150 : 113, 151 : 113, 152 : 113, 153 : 114, 154 : 114, 155 : 115, 156 : 116, 157 : 116, 158 : 117, 159 : 117, 160 : 118, 161 : 118, 162 : 119, 163 : 120, 164 : 120, 165 : 121, 166 : 122, 167 : 122, 168 : 123, 169 : 123, 170 : 124, 171 : 124, 172 : 125, 173 : 125, 174 : 126, 175 : 126, 176 : 127, 177 : 127, 178 : 128, 179 : 129, 180 : 129, 181 : 130, 182 : 130, 183 : 131, 184 : 131, 185 : 132, 186 : 133, 187 : 133, 188 : 134, 189 : 134, 190 : 135, 191 : 135, 192 : 136, 193 : 137, 194 : 137, 195 : 138, 196 : 138, 197 : 138, 198 : 140, 199 : 140, 200 : 140, 201 : 141, 202 : 142, 203 : 142, 204 : 143, 205 : 143, 206 : 144, 207 : 144, 208 : 145, 209 : 146, 210 : 146, 211 : 146, 212 : 147, 213 : 147, 214 : 149, 215 : 149, 216 : 150, 217 : 150, 218 : 151, 219 : 151, 220 : 152, 221 : 152, 222 : 153, 223 : 153, 224 : 154, 225 : 154, 226 : 155, 227 : 156, 228 : 156, 229 : 157, 230 : 158, 231 : 158, 232 : 159, 233 : 159, 234 : 160, 235 : 160, 236 : 161, 237 : 162, 238 : 162, 239 : 163, 240 : 163, 241 : 163, 242 : 165, 243 : 165, 244 : 165, 245 : 166, 246 : 166, 247 : 167, 248 : 167, 249 : 168, 250 : 169, 251 : 169, 252 : 170, 253 : 170, 254 : 171, 255 : 172, 256 : 172, 257 : 173, 258 : 173, 259 : 173, 260 : 174, 261 : 175, 262 : 176, 263 : 176, 264 : 177, 265 : 177, 266 : 178, 267 : 178, 268 : 179, 269 : 179, 270 : 180, 271 : 181, 272 : 181, 273 : 181, 274 : 182, 275 : 183, 276 : 183, 277 : 184, 278 : 184, 279 : 185, 280 : 186, 281 : 186, 282 : 187, 283 : 187, 284 : 188, 285 : 188, 286 : 189, 287 : 190, 288 : 190, 289 : 191, 290 : 191, 291 : 192, 292 : 192, 293 : 193, 294 : 193, 295 : 194, 296 : 195, 297 : 195, 298 : 196, 299 : 196, 300 : 197, 301 : 197, 302 : 198, 303 : 199, 304 : 199, 305 : 200, 306 : 201, 307 : 201, 308 : 201, 309 : 202, 310 : 203, 311 : 203, 312 : 203, 313 : 205, 314 : 205, 315 : 205, 316 : 206, 317 : 206, 318 : 207, 319 : 208, 320 : 208, 321 : 209, 322 : 209, 323 : 210, 324 : 210, 325 : 211, 326 : 212, 327 : 212, 328 : 213, 329 : 213, 330 : 214, 331 : 214, 332 : 215, 333 : 216, 334 : 216, 335 : 217, 336 : 217, 337 : 218, 338 : 218, 339 : 219, 340 : 219, 341 : 220, 342 : 221, 343 : 221, 344 : 222, 345 : 222, 346 : 223, 347 : 224, 348 : 224, 349 : 225, 350 : 225, 351 : 226, 352 : 226, 353 : 227, 354 : 227, 355 : 228, 356 : 229, 357 : 229, 358 : 230, 359 : 230, 360 : 231, 361 : 231, 362 : 232, 363 : 232, 364 : 233, 365 : 234, 366 : 234, 367 : 235, 368 : 235, 369 : 236, 370 : 236, 371 : 237, 372 : 237, 373 : 238, 374 : 238, 375 : 239, 376 : 240, 377 : 240, 378 : 241, 379 : 242, 380 : 242, 381 : 243, 382 : 243, 383 : 244, 384 : 244, 385 : 245, 386 : 246, 387 : 246, 388 : 246, 389 : 247, 390 : 248, 391 : 248, 392 : 249, 393 : 249, 394 : 250, 395 : 251, 396 : 251, 397 : 252, 398 : 252, 399 : 253, 400 : 253, 401 : 254, 402 : 255, 403 : 255, 404 : 255, 405 : 256, 406 : 257, 407 : 258, 408 : 258, 409 : 258, 410 : 259, 411 : 260, 412 : 260, 413 : 260, 414 : 261, 415 : 262, 416 : 263, 417 : 263, 418 : 264, 419 : 264, 420 : 265, 421 : 265, 422 : 266, 423 : 266, 424 : 267, 425 : 267, 426 : 268, 427 : 269, 428 : 269, 429 : 270, 430 : 271, 431 : 271, 432 : 271, 433 : 273, 434 : 273, 435 : 273, 436 : 274, 437 : 275, 438 : 275, 439 : 275, 440 : 276, 441 : 277, 442 : 277, 443 : 278, 444 : 279, 445 : 279, 446 : 280, 447 : 280, 448 : 281, 449 : 282, 450 : 282, 451 : 283, 452 : 283, 453 : 284, 454 : 284, 455 : 285, 456 : 285, 457 : 286, 458 : 287, 459 : 287, 460 : 287, 461 : 288, 462 : 288, 463 : 289, 464 : 290, 465 : 290, 466 : 291, 467 : 292, 468 : 292, 469 : 293, 470 : 293, 471 : 294, 472 : 294, 473 : 295, 474 : 295, 475 : 296, 476 : 297, 477 : 297, 478 : 298, 479 : 298, 480 : 299, 481 : 299, 482 : 300, 483 : 300, 484 : 301, 485 : 302, 486 : 303, 487 : 303, 488 : 304, 489 : 304, 490 : 305, 491 : 305, 492 : 306, 493 : 306, 494 : 307, 495 : 307, 496 : 308, 497 : 308, 498 : 309, 499 : 310, 500 : 310, 501 : 311, 502 : 312, 503 : 312, 504 : 313, 505 : 313, 506 : 314, 507 : 314, 508 : 315, 509 : 316, 510 : 316, 511 : 316, 512 : 318, 513 : 318, 514 : 318, 515 : 319, 516 : 319, 517 : 320, 518 : 321, 519 : 321, 520 : 322, 521 : 322, 522 : 323, 523 : 323, 524 : 324, 525 : 324, 526 : 325, 527 : 326, 528 : 326, 529 : 327, 530 : 327, 531 : 328, 532 : 329, 533 : 329, 534 : 330, 535 : 330, 536 : 331, 537 : 332, 538 : 332, 539 : 333, 540 : 333, 541 : 334, 542 : 335, 543 : 335, 544 : 335, 545 : 337, 546 : 337, 547 : 337, 548 : 338, 549 : 338, 550 : 339, 551 : 340, 552 : 340, 553 : 340, 554 : 341, 555 : 342, 556 : 342, 557 : 344, 558 : 344, 559 : 344, 560 : 344, 561 : 346, 562 : 346, 563 : 347, 564 : 347, 565 : 348, 566 : 348, 567 : 349, 568 : 350, 569 : 350, 570 : 350, 571 : 351, 572 : 352, 573 : 352, 574 : 353, 575 : 354, 576 : 354, 577 : 355, 578 : 355, 579 : 356, 580 : 357, 581 : 357, 582 : 358, 583 : 359, 584 : 359, 585 : 359, 586 : 360, 587 : 360, 588 : 361, 589 : 361, 590 : 362, 591 : 363, 592 : 363, 593 : 364, 594 : 365, 595 : 365, 596 : 366, 597 : 366, 598 : 366, 599 : 368, 600 : 368, 601 : 369, 602 : 369, 603 : 370, 604 : 371, 605 : 371, 606 : 371, 607 : 372, 608 : 372, 609 : 374, 610 : 374, 611 : 375, 612 : 375, 613 : 375, 614 : 376, 615 : 376, 616 : 377, 617 : 378, 618 : 378, 619 : 379, 620 : 379, 621 : 380, 622 : 381, 623 : 381, 624 : 382, 625 : 382, 626 : 383, 627 : 383, 628 : 384, 629 : 385, 630 : 385, 631 : 385, 632 : 386, 633 : 387, 634 : 387, 635 : 389, 636 : 388, 637 : 389, 638 : 390, 639 : 390, 640 : 391, 641 : 392, 642 : 392, 643 : 392, 644 : 393, 645 : 394, 646 : 394, 647 : 395, 648 : 396, 649 : 396, 650 : 397, 651 : 398, 652 : 397, 653 : 399, 654 : 399, 655 : 399, 656 : 400, 657 : 401, 658 : 401, 659 : 402, 660 : 402, 661 : 403, 662 : 403, 663 : 404, 664 : 405, 665 : 405, 666 : 406, 667 : 406, 668 : 407, 669 : 407, 670 : 408, 671 : 409, 672 : 410, 673 : 410, 674 : 410, 675 : 411, 676 : 412, 677 : 413, 678 : 413, 679 : 413, 680 : 414, 681 : 414, 682 : 415, 683 : 416, 684 : 416, 685 : 416, 686 : 418, 687 : 418, 688 : 419, 689 : 419, 690 : 420, 691 : 420, 692 : 421, 693 : 422, 694 : 422, 695 : 423, 696 : 423, 697 : 424, 698 : 424, 699 : 424, 700 : 425, 701 : 426, 702 : 427, 703 : 427, 704 : 428, 705 : 428, 706 : 429, 707 : 429, 708 : 430, 709 : 430, 710 : 431, 711 : 432, 712 : 432, 713 : 433, 714 : 433, 715 : 434, 716 : 434, 717 : 436, 718 : 436, 719 : 436, 720 : 437, 721 : 438, 722 : 438, 723 : 439, 724 : 439, 725 : 440, 726 : 440, 727 : 441, 728 : 441, 729 : 442, 730 : 442, 731 : 443, 732 : 444, 733 : 444, 734 : 445, 735 : 446, 736 : 446, 737 : 447, 738 : 448, 739 : 448, 740 : 448, 741 : 449, 742 : 449, 743 : 450, 744 : 451, 745 : 451, 746 : 452, 747 : 453, 748 : 453, 749 : 453, 750 : 454, 751 : 455, 752 : 455, 753 : 456, 754 : 456, 755 : 457, 756 : 457, 757 : 458, 758 : 459, 759 : 459, 760 : 460, 761 : 460, 762 : 461, 763 : 462, 764 : 462, 765 : 463, 766 : 464, 767 : 464, 768 : 464, 769 : 465, 770 : 465, 771 : 466, 772 : 467, 773 : 467, 774 : 468, 775 : 469, 776 : 469, 777 : 469, 778 : 470, 779 : 470, 780 : 471, 781 : 472, 782 : 473, 783 : 473, 784 : 474, 785 : 474, 786 : 475, 787 : 476, 788 : 476, 789 : 476, 790 : 478, 791 : 478, 792 : 478, 793 : 479, 794 : 479, 795 : 480, 796 : 481, 797 : 481, 798 : 482, 799 : 482, 800 : 483, 801 : 483, 802 : 484, 803 : 485, 804 : 486, 805 : 486, 806 : 486, 807 : 487, 808 : 487, 809 : 488, 810 : 489, 811 : 490, 812 : 489, 813 : 490, 814 : 491, 815 : 492, 816 : 492, 817 : 493, 818 : 493, 819 : 494, 820 : 494, 821 : 495, 822 : 496, 823 : 497, 824 : 497, 825 : 497, 826 : 498, 827 : 499, 828 : 499, 829 : 500, 830 : 500, 831 : 502, 832 : 501, 833 : 503, 834 : 503, 835 : 504, 836 : 504, 837 : 505, 838 : 505, 839 : 506, 840 : 506, 841 : 507, 842 : 508, 843 : 508, 844 : 508, 845 : 509, 846 : 510, 847 : 511, 848 : 511, 849 : 512, 850 : 512, 851 : 512, 852 : 513, 853 : 514, 854 : 514, 855 : 515, 856 : 515, 857 : 516, 858 : 517, 859 : 517, 860 : 518, 861 : 519, 862 : 519, 863 : 521, 864 : 520, 865 : 521, 866 : 521, 867 : 523, 868 : 523, 869 : 523, 870 : 524, 871 : 524, 872 : 525, 873 : 526, 874 : 526, 875 : 527, 876 : 527, 877 : 528, 878 : 528, 879 : 529, 880 : 529, 881 : 530, 882 : 531, 883 : 531, 884 : 532, 885 : 532, 886 : 533, 887 : 533, 888 : 534, 889 : 535, 890 : 536, 891 : 536, 892 : 537, 893 : 537, 894 : 537, 895 : 538, 896 : 539, 897 : 539, 898 : 540, 899 : 540, 900 : 541, 901 : 541, 902 : 542, 903 : 543, 904 : 544, 905 : 544, 906 : 544, 907 : 545, 908 : 547, 909 : 547, 910 : 547, 911 : 547, 912 : 548, 913 : 549, 914 : 550, 915 : 550, 916 : 550, 917 : 552, 918 : 551, 919 : 553, 920 : 553, 921 : 554, 922 : 554, 923 : 555, 924 : 555, 925 : 556, 926 : 556, 927 : 558, 928 : 557, 929 : 558, 930 : 558, 931 : 559, 932 : 560, 933 : 560, 934 : 562, 935 : 561, 936 : 562, 937 : 563, 938 : 563, 939 : 564, 940 : 565, 941 : 565, 942 : 566, 943 : 566, 944 : 567, 945 : 567, 946 : 567, 947 : 569, 948 : 569, 949 : 570, 950 : 570, 951 : 570, 952 : 571, 953 : 572, 954 : 573, 955 : 573, 956 : 574, 957 : 574, 958 : 575, 959 : 575, 960 : 576, 961 : 576, 962 : 577, 963 : 578, 964 : 578, 965 : 579, 966 : 580, 967 : 580, 968 : 580, 969 : 581, 970 : 583, 971 : 582, 972 : 583, 973 : 584, 974 : 584, 975 : 584, 976 : 586, 977 : 586, 978 : 586, 979 : 587, 980 : 588, 981 : 588, 982 : 589, 983 : 590, 984 : 590, 985 : 590, 986 : 591, 987 : 592, 988 : 592, 989 : 593, 990 : 594, 991 : 594, 992 : 594, 993 : 595, 994 : 595, 995 : 596, 996 : 597, 997 : 597, 998 : 599, 999 : 599, 1000 : 599}
