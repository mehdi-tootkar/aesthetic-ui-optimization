figma.showUI(__html__, { visible: false });

figma.ui.onmessage = async (msg) => {
  if (msg.type === 'apply-action') {
    const { action_id, target_id, params } = msg.data;
    const node = figma.getNodeById(target_id);
    if (node && action_id === 0 && node.paddingLeft !== undefined) {
      node.paddingLeft += params.delta;
      node.paddingRight += params.delta;
    }
    const state = getUIState();
    const image = await exportFrameImage();
    figma.ui.postMessage({ type: 'task-completed', state, image });
  }
};

function getUIState() {
  const frame = figma.currentPage.selection[0];
  return {
    id: frame.id,
    width: frame.width,
    height: frame.height,
    elements: frame.children.map(c => ({
      id: c.id,
      type: c.type,
      x: c.x / frame.width,
      y: c.y / frame.height,
      width: c.width / frame.width,
      height: c.height / frame.height
    }))
  };
}

async function exportFrameImage() {
  const frame = figma.currentPage.selection[0];
  return await frame.exportAsync({ format: 'JPG', constraint: { type: 'SCALE', value: 1 } });
}
