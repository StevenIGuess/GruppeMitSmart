import sys, subprocess, shlex

def stream2string(stream):
  s = str()
  for cc in stream.decode():
    s += cc
  return s.rstrip()

def mysubprocess(cmd_line):
  cmd_args = shlex.split(cmd_line)
  thispipe = subprocess.Popen(cmd_args,
                              stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE)
  stdout_encoded_stream, stderr_encoded_stream = thispipe.communicate(0)
  rc = thispipe.returncode
  stdout_str = stream2string(stdout_encoded_stream)
  stderr_err = stream2string(stderr_encoded_stream)
  return rc, stdout_str, stderr_err

def mysubprocess_expect(cmd_line,expected_err_code,expected_err_msg = None):
  rc, stdout_str, stderr_str = mysubprocess(cmd_line)
  if rc != expected_err_code:
    sys.stderr.write(\
      '{}: cmd_line="{}", err_code = {} != {} = expected_err_code\n'
       .format(sys.argv[0],cmd_line,rc,expected_err_code))
    exit(1)
  if expected_err_msg and stderr_str != expected_err_msg:
    sys.stderr.write(\
      '{}: cmd_line="{}",\nstderr_str = "{}" !=\n       \
      "{}" = expected_err_msg\n'
       .format(sys.argv[0],cmd_line,stderr_str,expected_err_msg))
    exit(1)
