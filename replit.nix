{ pkgs }: {
  deps = [
    pkgs.python310
    pkgs.tesseract
    pkgs.poppler
    pkgs.ffmpeg
    pkgs.git
  ];
}
