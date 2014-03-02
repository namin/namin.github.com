---
layout: post
title: Branching
codemirror: javascript
---

Some variations on
_["Branching is Fun"](http://ricardocabello.com/blog/post/680)_ by
[@mr_doob](http://twitter.com/mr_doob).

<script>
var live_snippets = [];
</script>

<textarea id="snippet-header" style="display:none;">
&lt;!DOCTYPE HTML&gt;
&lt;html lang="en"&gt;
	&lt;head&gt;
		&lt;title&gt;Branching - 00&lt;/title&gt;
		&lt;meta charset="utf-8"&gt;
		&lt;meta name="viewport" content="width=device-width, user-scalable=no, minimum-scale=1.0, maximum-scale=1.0"&gt;
		&lt;style type="text/css"&gt;
			body { background-color: #000000; margin: 0px; overflow: hidden; }
		&lt;/style&gt;
	&lt;/head&gt;
	&lt;body&gt;
		&lt;div id="container"&gt;&lt;/div&gt;
		&lt;script type="text/javascript"&gt;
</textarea>

<textarea id="snippet-footer" style="display:none;">
		&lt;/script&gt;
	&lt;/body&gt;
&lt;/html&gt;
</textarea>


<iframe class="viewcode" id="viewcode-branching-00"></iframe>
<textarea class="live" id="code-branching-00" name="code-branching-00">
var container, canvas, context;
var WIDTH, HEIGHT;
var branches, mouseX, mouseY;
init();
setInterval(loop, 1000/60);
function init() {
  container = document.getElementById('container');
  WIDTH = window.innerWidth;
  HEIGHT = window.innerHeight;
  var canvas = document.createElement("canvas");
  canvas.width = WIDTH;
  canvas.height = HEIGHT;
  container.appendChild(canvas);
  context = canvas.getContext("2d");
  context.fillStyle = "rgb(0, 0, 0)";
  context.fillRect (0, 0, WIDTH, HEIGHT);
  branches = [];
  window.addEventListener('mousemove', onWindowMouseMove, false);
}
function onWindowMouseMove(event) {
  mouseX = event.clientX;
  mouseY = event.clientY;
}
function loop() {
  if (branches.length &lt; 500) {
    branches.push(new Branch(mouseX, mouseY));
  }
  context.beginPath();
  context.strokeStyle = "#f80";
  for (var i = 0; i &lt; branches.length; i++) {
    var branch = branches[i];
    branch.life ++;
    if (branch.life &gt; 500) {
      branches.shift();
      continue;
    }
    context.moveTo(branch.x, branch.y);
    branch.rw += Math.random() - 0.5;
    branch.x += Math.cos(branch.rw);
    branch.y += Math.sin(branch.rw);
    context.lineTo(branch.x, branch.y);
  }
  context.stroke();
  context.closePath();
  context.fillStyle = "rgba(50, 0, 25, 0.1)";
  context.fillRect (0, 0, WIDTH, HEIGHT);
}
var Branch = function(x, y) {
  this.life = 0;
  this.x = x;
  this.y = y;
  this.rw = Math.random() * 360;
};
</textarea>

<script>
live_snippets.push('code-branching-00');
</script>

<iframe class="viewcode" id="viewcode-branching-01"></iframe>
<textarea class="live" id="code-branching-01" name="code-branching-01">
var container, canvas, context;
var WIDTH, HEIGHT;
var branches, mouseX, mouseY;
init();
setInterval(loop, 1000/60);
function init()
{
  container = document.getElementById('container');
  WIDTH = window.innerWidth;
  HEIGHT = window.innerHeight;
  var canvas = document.createElement("canvas");
  canvas.width = WIDTH;
  canvas.height = HEIGHT;
  container.appendChild(canvas);
  context = canvas.getContext("2d");
  context.fillStyle = "rgb(0, 0, 0)";
  context.fillRect (0, 0, WIDTH, HEIGHT);
  branches = [];
  window.addEventListener('mousedown', onWindowMouseDown, false);
}
function onWindowMouseDown(e)
{
  if (!e) e = window.event;
  mouseX = e.clientX;
  mouseY = e.clientY;
  branches.push(new Branch(mouseX, mouseY, 1000));
}
function loop()
{
  context.beginPath();
  context.strokeStyle = "#ff0";
  for (var i = 0; i &lt; branches.length; i++)
  {
    var branch = branches[i];
    branch.life ++;
    context.moveTo(branch.x, branch.y);
    branch.rw += Math.random() - 0.5;
    branch.x += Math.cos(branch.rw) * branch.speed;
    branch.y += Math.sin(branch.rw) * branch.speed;
    context.lineTo(branch.x, branch.y);
    if (branch.life > branch.max_life ||
        branch.x &lt; 0 || branch.y &lt; 0 ||
        branch.x &gt; WIDTH || branch.y &gt; HEIGHT)
      branches.splice(i,1);
    if (Math.random() &gt; 0.95 && branches.length &lt; 1000)
    {
      branches.push(new Branch(branch.x, branch.y, branch.max_life / 10));
    }
  }
  context.stroke();
  context.closePath();
  context.fillStyle = "rgba(0, 25, 25, 0.05)";
  context.fillRect (0, 0, WIDTH, HEIGHT);
}
var Branch = function(x, y, max_life)
{
  this.life = 0;
  this.max_life = max_life;
  this.speed = Math.random() + 1;
  this.x = x;
  this.y = y;
  this.rw = Math.random() * 360;
};
</textarea>

<script>
live_snippets.push('code-branching-01');
</script>

<iframe class="viewcode" id="viewcode-branching-01-spite"></iframe>
<textarea class="live" id="code-branching-01-spite" name="code-branching-01-spite">
var container, canvas, context;
var WIDTH, HEIGHT;
var branches, mouseX, mouseY;
init();
setInterval(loop, 1000/60);
function init()
{
  container = document.getElementById('container');
  WIDTH = window.innerWidth;
  HEIGHT = window.innerHeight;
  canvas = document.createElement("canvas");
  canvas.width = WIDTH;
  canvas.height = HEIGHT;
  //canvas.style.display = 'none';
  container.appendChild(canvas);
  context = canvas.getContext("2d");
  context.fillStyle = "rgb(0, 0, 0, 0.1)";
  context.fillRect (0, 0, WIDTH, HEIGHT);
  branches = [];
  window.addEventListener('mousedown', onWindowMouseDown, false);
}
function onWindowMouseDown(e)
{
  if (!e) e = window.event;
  mouseX = e.clientX;
  mouseY = e.clientY;
  branches.push(new Branch(mouseX, mouseY, 1000));
}
function loop()
{
  var s = -4;
  context.drawImage( canvas, -s, -s, WIDTH + 2 * s, HEIGHT + 2 * s );
  context.fillStyle = "rgba(0, 25, 25, 0.05)";
  context.fillRect (0, 0, WIDTH, HEIGHT);
  context.beginPath();
  context.strokeStyle = "#ff0";
  for (var i = 0; i &lt; branches.length; i++)
  {
    var branch = branches[i];
    branch.life ++;
    context.moveTo(branch.x, branch.y);
    branch.rw += Math.random() - 0.5;
    branch.x += Math.cos(branch.rw) * branch.speed;
    branch.y += Math.sin(branch.rw) * branch.speed;
    context.lineTo(branch.x, branch.y);
    if (branch.life > branch.max_life ||
       branch.x &lt; 0 || branch.y &lt; 0 ||
       branch.x &gt; WIDTH || branch.y &gt; HEIGHT)
       branches.splice(i,1);
    if (Math.random() > 0.9 && branches.length < 1000)
    {
      branches.push(new Branch(branch.x, branch.y, branch.max_life / 10));
    }
  }
  context.stroke();
  context.closePath();
}
var Branch = function(x, y, max_life)
{
  this.life = 0;
  this.max_life = max_life;
  this.speed = Math.random() + 2;
  this.x = x;
  this.y = y;
  this.rw = Math.random() * 360;
};
</textarea>

<script>
live_snippets.push('code-branching-01-spite');
</script>

<script>
window.onload = function() {
  for (var i=0; i<live_snippets.length; i++) {
    (function(snippet) {
    var delay;
    var editor = CodeMirror.fromTextArea(document.getElementById(snippet), {
    mode: 'javascript',
    tabMode: 'indent',
    viewportMargin: Infinity,
    gutters: ["CodeMirror-lint-markers"],
    lint: true
    });
    editor.on('change', function() {
      clearTimeout(delay);
      delay = setTimeout(updatePreview, 300);
    });
    var header = document.getElementById('snippet-header');
    var footer = document.getElementById('snippet-footer');
    function updatePreview() {
      var previewFrame = document.getElementById('view'+snippet);
      var preview =  previewFrame.contentDocument ||  previewFrame.contentWindow.document;
      preview.open();
      preview.write(header.value+editor.getValue()+footer.value);
      preview.close();
    }
    setTimeout(updatePreview, 300);
   })(live_snippets[i]);
 }
}
</script>
